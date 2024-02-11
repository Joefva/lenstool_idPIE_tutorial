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




## predT0.h

This script is in `./utils`, and serves to yield a reference pivot ICM temperature, in the ``X-ray`` section, where keywords ``Temp0`` and ``Jz_array`` are proper to the hydrostatic X-ray profiles (type ``2``).

``Temp0`` is the pivot temperature model, eq. (17) in 
`Allingham+23b <https://arxiv.org/abs/2309.07076>`_:
:math:`T_0(z) = T_{500,c} (z) T_{\rm ref}`.
It may be computed using routine ``predT``:

.. code-block:: console
	
	predT0 <redshift> <model_type> <M_500,c>
	
where the mass
:math:`M_{500,c}` is in
:math:`M_{\odot}`, and the ``<model_type>`` corresponds to the regression used for
:math:`P_e (n_e)`. By defult, use ``polyEv1`` for the latter.

``Jz_array`` indicates how to compute the Jz function, relating the potential to the ICM density 
:math:`n_e`. 
It takes three arguments:

- An integer. ``0``: do not perform the computation. ``1``: perform it.

- A string for the model type. By default, use ``polyE``.

- A second string for the name of the output array. If the array is not computed (``0``), this array must already exist.

