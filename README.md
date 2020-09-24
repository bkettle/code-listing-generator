# Code Listing Generator

This will generate a PDF documenting code in the given folder.

## To install:

`pip3 install code-listing-generator`

(requires python3)

## To use:

* Navigate to the directory whose files you want to list
* run the command `generate-code-listing`
* this will ask a few questions and then create a file inside the `code-writeup/` subdirectory of the current folder (it will make this folder)
* If you have a local LaTeX installation, you can `cd code-writeup` and then `pdflatex code-writeup`, or if you use overleaf you can upload/paste the file `code-writeup/writeup.tex` into overleaf. 

If anything seems broken or you want me to change anything, open an issue (or submit a PR fixing it, if you want)
