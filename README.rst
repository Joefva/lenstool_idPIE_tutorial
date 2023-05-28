Template for the Read the Docs tutorial
=======================================

This GitHub template includes fictional Python library
with some basic Sphinx docs.

Read the tutorial here:

https://docs.readthedocs.io/en/stable/tutorial/


Compile html: 
sphinx-build -b html docs/source/ docs/build/html

# For the "API", one can refer to the full code of Lenstool, if this is in this directory.



# cf. 'Sphinx-CPP-TriangleLib-1.1', generated with:
sphinx-build -b xml docs/sphinx/source docs/sphinx/build/xml
sphinx-build -b html docs/sphinx/source docs/sphinx/build/html

# and work from there. And see: https://leimao.github.io/blog/CPP-Documentation-Using-Sphinx/
