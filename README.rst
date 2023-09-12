Read the Docs: lenstool
=========================

* Read the tutorial here:
https://docs.readthedocs.io/en/stable/tutorial/

* Install Sphinx:
https://smobsc.readthedocs.io/en/stable/usage/installation.html

* Compile html (may also do latex or xml): 
sphinx-build -b html docs/sphinx/source docs/sphinx/build/html

* If some .md files are included, use myst_parser:
pip install myst-parser

* You can open the compiled ReadTheDocs files in docs/sphinx/build/html/

* For the "API", one can refer to the full code of Lenstool, if this is in this directory.
And see: https://leimao.github.io/blog/CPP-Documentation-Using-Sphinx/ for the API in C/C++.
