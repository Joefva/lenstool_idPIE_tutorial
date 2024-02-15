# grid

Defines some parameters such has the number of potential mode, the total number of potential mode that are going to be tested, the grid mode, and the number of rows and columns in the grid.


If no counter image is found for an image defined in the runmode section with the [image]() or [source]() keywords, then the following warning message is printed out: "WARN: There were missed images probably due to the grid resolution." 
In this case, you can try to increase the grid resolution with the [nombre]() keyword, or adopt a polar geometry for the grid with the [polaire]() keyword.



## number int

Represents the number of points of the grid used to invert the lens equation (from Source Plane to Image Plane).  An even number,   between 10 and 128 is required. Default: `int= 30`. 

## number (new syntax)

- Syntax : `number N`


- Parameters: 
    - `N`, integer: Number of points that is used to define the grid to invert the lens equation (from Source Plane to Image Plane). An even number, between 10 and 128 is required. Default: `30`.


## polar int

Set the grid to a polar shape if `int= 1`, else it takes a rectangular shape. Polar shape is advised if the main clump is centered on (0,0). Default: int=0 meaning that the program will used a rectangular grid. Interest: used to predict radial images in axi-symetrical lens model. 


## nlens int

Set the number of clumps that defines the Lens Potential. The number of first identifier potential must be equal or larger than this number. If the  number of potentials is lower than nlentille then nlentille is set to the effectively read number of potentials. Default: `int=0`.


## nlens\_opt int

Set the number of clumps that will be optimized in the inverse mode. The number of first identifiers potential and limit must be equal or larger than this number otherwise nlens_opt is set to the number of limit identifier read. Moreover one should have nlens_opt ≤ nlentille. Default: `int=0`.


## nlens\_crit int

Set the number of clumps for which the critical lines must be calculated. Only used for the snake algorithm (defined in section [cline]()).
