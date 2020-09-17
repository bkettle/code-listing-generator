import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="code-listing-generator", # Replace with your own username
    version="0.0.3",
    author="Ben Kettle",
    author_email="",
    description="Creates a LaTeX document with code from all files in the current directory",
    url="https://github.com/bkettle/code-listing-generator",
    packages=setuptools.find_packages(),
    scripts=['scripts/generate-code-listing'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
