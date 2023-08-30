# Utils

## bayesImage

This tool generate a list of images catalogs in a new directory `image`. It computes as many catalogs as lines in the `bayes.dat` files. 

```
Syntax : bayesImage [OPTION] <.par>
Available OPTIONS:
 -b : compute images of system barycenter [default]
 -i : compute counter images, image per image
```

Argument:
The parameter file used for the optimization. Do not use the best.par or bestopt.par produced after optimization.

Options:
- `-b` Uses the image catalog specified with the `multfile` keyword in the `image` section. The barycenter of each system of images is computed and its counter images are found with the grid technique.
- `-i` Uses the image catalog specified with the `image` keyword in the `runmode` section. The counter images for each individual image is computed with the grid technique.

## bayesImage.sh

This script located in the directory `./perl`, calls the _bayesImage_ tool, and concatenates all the multiple images catalogs in one file `bayesImage.all`, and display it in DS9 if opened. 

```
Syntax : bayesImage.sh <.par>
```

Argument:
The parameter file used for the optimization. Do not use the best.par or bestopt.par produced after optimization.

The call to `bayesImage` is done with option `-b`. 

Note that only the first 5000 images are transferred to DS9. This number is set at the beginning of the  script `bayesImage.sh`.



