grid
====

Defines some parameters such has the number of potential mode, the total number of potential mode that are going to be tested, the grid mode, and the number of rows and columns in the grid.


If no counter image is found for an image defined in the runmode section with the [image]() or [source]() keywords, then the following warning message is printed out: "WARN: There were missed images probably due to the grid resolution." 
In this case, you can try to increase the grid resolution with the [nombre]() keyword, or adopt a polar geometry for the grid with the [polaire]() keyword.




number
------

.. admonition:: Syntax

   ``number N``


- Parameters: 
    - ``N``, integer: Number of points that is used to define the grid to invert the lens equation (from Source Plane to Image Plane). An even number, between 10 and 128 is required. Default: ``30``.
 

polar
-----

.. admonition:: Syntax

   ``polar b``


- Parameters: 
    - ``b``, boolean: If ``b=1`` the grid used to predict multiple images is polar, else a rectangular grid is used. The polar shape is advised if the main clump is centered on (0,0). It allows to predict radial images in axi-symetrical lens model. Default: ``b=0``


nlens
-----

.. admonition:: Syntax

   ``nlens N``

- Parameters: 
    - ``N``, integer: Set the number of clumps that defines the Lens Potential. The number of first identifier potential must be equal or larger than this number. If the  number of potentials is lower than ``N`` then ``N`` is set to the effectively read number of potentials. Default: ``N=0``



nlens_opt
---------

.. admonition:: Syntax

   ``nlens_opt N``

- Parameters: 
    - ``N``, integer: Set the number of clumps that will be optimized in the inverse mode. The number of first identifiers potential and limit must be equal or larger than this number otherwise nlens_opt is set to the number of limit identifier read. Moreover the number of optimised lens should inferior or equal to the number of lens defined at ``nlens``. Default: ``N=0``.


nlens_crit
----------

.. admonition:: Syntax

   ``nlens_crit N``

- Parameters: 
    - ``N``, integer: Set the number of clumps for which the critical lines must be calculated. Only used for the snake algorithm. Default: ``N=0``.
