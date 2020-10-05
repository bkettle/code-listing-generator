import os
import jinja2
import argparse
from jinja2 import Template
import pyperclip
import subprocess

# set up jinja
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{', block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(__location__)
)

def gen_filenames(prompt=False, path=".", depth=0, recursive=False):
    # iterate through all files and directories in the selected directory
    # save files and dirs
    this_dir_files = []
    this_dir_subdirs = []
    for filename in os.listdir(path=path):
        filename = os.path.join(path, filename)

        if os.path.isfile(filename):
            this_dir_files.append(filename)
        if os.path.isdir(filename) and recursive:
            this_dir_subdirs.append(filename)

    # ask user to confirm each file in this directory
    for filename in this_dir_files:
        if prompt:
            if input("| "*depth + f"include file {filename}? (y) ") != 'y':
                continue
        yield filename

    # ask user if we should go into the next dir
    for dirname in this_dir_subdirs:
        if prompt:
            if input("| "*depth + f"enter directory {dirname}? (y) ") != 'y':
                continue
        # yield each file that the user chooses to accept from a lower level
        dirname = os.path.join(dirname)
        for filename in gen_filenames(prompt=prompt, path=dirname, depth=depth+1, recursive=recursive):
            yield filename

def generate(name, title, recursive=False, prompt=False, make=True, copy=False, print_tex=False):
    if make:
        # make the directory to hold the writeup
        try:
            os.mkdir("code-writeup")
        except FileExistsError:
            confirm = input("Directory 'code-writeup' exists. Delete it? (y) ")
            if confirm != 'y':
                print("okay, exiting")
                quit()
    
    tex_to_insert = ""
    for filename in gen_filenames(recursive=recursive, prompt=prompt):
        with open(filename, "r") as f:
            file_contents = f.read()
    
        # make sure to escape underscores
        tex_to_insert += "\\subsection{\\tt{\detokenize{" + filename + "}}}\n"
        tex_to_insert += "\\begin{lstlisting}\n"
        tex_to_insert += file_contents
        tex_to_insert += "\n\\end{lstlisting}\n"
    
    template = latex_jinja_env.get_template('template.tex')
    finished = template.render(name=name, doctitle=title, content=tex_to_insert)
   
    # deal with the output according to input flags
    if print_tex:
        print(finished)
    if make:
        with open("code-writeup/writeup.tex", "w") as f:
            f.write(finished)
        FNULL = open(os.devnull, 'w')
        p = subprocess.Popen(['pdflatex', 'writeup.tex'], stdout=FNULL, stderr=subprocess.STDOUT, cwd="./code-writeup/")
        print("PDF generated. See code-writeup directory")
    if copy:
        pyperclip.copy(finished)
        print("LaTeX copied to clipboard")

def main():
    parser = argparse.ArgumentParser(description='Generate LaTeX for code listing')
    parser.add_argument('--recursive', '-r', action='store_true', help="traverse into subfolders of the current folder")
    parser.add_argument('--prompt', '-p', action='store_true', help="prompt user to select folders to enter and files to include (default: include all files)")
    parser.add_argument('--make', '-m', action='store_true', help="Create a folder and run pdflatex inside it")
    parser.add_argument('--copy', '-c', action='store_true', help="copy the text to the clipboard using pyperclip")
    args = parser.parse_args()

    # get user and document info
    name = input("What's your name? ")
    title = input("What should this document be titled? ")

    # we want to print out the tex code if it's not being saved (as part of make)
    print_tex = not args.make

    generate(name, title, recursive=args.recursive, prompt=args.prompt, make=args.make, copy=args.copy, print_tex=print_tex)

if __name__ == "__main__":
    main()
