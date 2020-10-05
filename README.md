# Code Listing Generator

This will generate a PDF documenting code in the given folder.

## To install:

`pip3 install code-listing-generator`

(requires python3)

## To use:

* Navigate to the directory containing files (or subdirectories with more files) that you want to include in the listing. 
* run the command `generate-code-listing`. There are a few options you can use here, see below. 
	* If you want to be able to select files from all subdirectories of the current directory, and have the result copied to your clipboard (for example, to paste into overleaf), I recommend you try `generate-code-listing -rpc`. 
	* If you have a local installation of LaTeX including PDFLatex, you can use `generate-code-listing -rpm` to instruct the program to make a `code-writeup` subdirectory of the current directory, save the code there, and compile it using `pdflatex`.

### Options:
If you forget these while using the program, you can run `generate-code-listing -h` to display a short version.

* `-r`: find files recursively. This instructs the program to look in all subdirectories of the current directory and include files found there.
* `-p`: prompt user for each file. This allows the user to select some files and not others to be included in the directory listing. If used in conjunction with `-r`, it asks whether the user would like to enter each subdirectory, preventing having to manual exclude lots of irrelevant files.
* `-c`: copy result to clipboard. This simply copies the generated result to the system clipboard, it should use the correct tool depending on OS. Relies on `pyperclip`, which requires `xclip` or `xsel` on Linux. Also prints the LaTeX output to STDOUT, in case the copying doesn't work or the clipboard contents gets lost on the way to Overleaf.
* `-m`: make. This instructs the program to create a new directory `code-writeup` and save the outputted file inside that folder as `writeup.tex`. It then compiles this into a PDF with `pdflatex`--the result will be in the `code-writeup` folder it created.

## Modifications
If anything seems broken or you want me to change anything, open an issue (or submit a PR fixing it, if you want)
