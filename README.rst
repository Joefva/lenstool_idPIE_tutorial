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

* VERSION is the current lenstool version. This is simply three numbers 'X.Y.Z'.

* Think of adding the Lenstool library path to LD_LIBRARY_PATH:

.. code-block:: console

	export LD_LIBRARY_PATH=/PATH_TO_LENSTOOL/lib:$LD_LIBRARY_PATH

* Also add the lenstool path, under the variable name 'LENSTOOL_DIR' to docs/sphinx/source/conf.py:

.. code-block:: console

	export LENSTOOL_DIR=/path_to_lenstool/

where you must replace `path_to_lenstool`.


* New syntax for all parameters:

Example:

.. code-block:: console

    keyword
    --------

    .. admonition:: Syntax

       ``keyword param1 param2 param3 ...``


    - Parameters: 
        - ``param1``, param1 type (ex int, float): Description of the parameter. Default: default value if relevant.
        - ``param2``, param2 type (ex int, float): Description of the parameter. Default: default value if relevant.
        - ``param3``, param3 type (ex int, float): Description of the parameter. Default: default value if relevant.

    

