import os
import jinja2
from jinja2 import Template

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

# make the directory to hold the writeup
try:
    os.mkdir("code-writeup")
except FileExistsError:
    confirm = input("Directory 'code-writeup' exists. Delete it? (y) ")
    if confirm != 'y':
        print("okay, exiting")
        quit()

# get user and document info
name = input("What's your name? ")
title = input("What should this document be titled? ")

def get_filenames():
    for filename in os.listdir():
        if os.path.isfile(filename):
            yield filename

tex_to_insert = ""
for filename in get_filenames():
    # make sure to escape underscores
    tex_to_insert += "\\subsection{\\tt{\detokenize{" + filename + "}}}\n"
    tex_to_insert += "\\lstinputlisting{../" + filename + "}\n\n"

template = latex_jinja_env.get_template('template.tex')
finished = template.render(name=name, doctitle=title, content=tex_to_insert)

with open("code-writeup/writeup.tex", "w") as f:
    f.write(finished)