# Code Listing Generator

This will generate a PDF documenting code in the given folder.

To install:

`pip install code-listing-generator`

(requires python3)

To use:

* Navigate to the directory whose files you want to list
* run the command `generate-code-listing`
* this will ask a few questions and then create a file inside the `code-writeup/` subdirectory of the current folder (it will make this folder)
* If you have a local LaTeX installation, you can `cd code-writeup` and then `pdfltex code-writeup`, or if you use overleaf you can upload/paste the file `code-writeup/writeup.tex` into overleaf. 

If you want me to change anything, open an issue.
