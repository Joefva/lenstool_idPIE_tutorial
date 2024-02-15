Read the Docs: lenstool
=========================

* Read the tutorial here:
https://docs.readthedocs.io/en/stable/tutorial/

* Install Sphinx:
https://smobsc.readthedocs.io/en/stable/usage/installation.html

* Compile html (may also do latex or xml): 

.. code-block:: console

	sphinx-build -b html docs/sphinx/source docs/sphinx/build/html

* If some .md files are included, use myst_parser:

.. code-block:: console

	pip install myst-parser

* You can open the compiled ReadTheDocs files in docs/sphinx/build/html/

* For the "API", we do not have documentation yet. One can refer to the full code of Lenstool, if it is in this directory, but Sphinx favours Python code. To create an API with C/C++, see: https://leimao.github.io/blog/CPP-Documentation-Using-Sphinx/.
