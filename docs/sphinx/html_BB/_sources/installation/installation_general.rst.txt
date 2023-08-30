Installation
=============

.. _installation:


Starting from version 8, you can install Lenstool using conda on Linux and Mac OSX. This will give you access to the Python wrapper

.. code-block:: console

        conda install -c conda-forge lenstool

.. code-block:: python

       import lenstool


On Ubuntu, you can also use the command `apt-get` from the command line.

.. code-block:: console

        apt-get install lenstool

On Mac OSX, you can use Macports

.. code-block:: console

        sudo port install lenstool

On Windows you can use Cygwin, following the procedure described 

Please note the following dependencies

* CFITSIO:  [attachment:cfitsio3280.tar.gz]  version must be at least 2.510.
* GSL: [attachment:gsl-1.9.tar.gz]
* WCSTOOLS (until version 7): [attachment:wcstools-3.8.4.tar.gz]
* WCSLIB (since version 8): [https://www.atnf.csiro.au/people/Mark.Calabretta/WCS/]
* LIBZMQ and CPPZMQ (until version 7): [https://github.com/zeromq/cppzmq#build-instructions]
* PGPLOT (deprecated): [http://www.astro.caltech.edu/~tjp/pgplot/]

They can be installed with the package managers

``GitLab`` installation
------------------------

To install lenstool directly from the source:

.. code-block:: console

   git clone https://git-cral.univ-lyon1.fr/lenstool/lenstool.git



.. note::

   TODO: HERE detail the installation if necessary
   

