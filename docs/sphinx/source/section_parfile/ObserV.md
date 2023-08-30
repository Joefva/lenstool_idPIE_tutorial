# `observ`

*Under this identifier is defined the different noise that can be added to a gravitational image, such as seeing or Poisson Noise.*

All these constants are used when the image mode `large iso` or `runmode pixel` representation is set.



## `noise int`

`int = 0`: if false  `int = 1`: is true

If true, add Poisson noise to the final image

## `sky float`

Mean value for the sky background

## `idum int`

Random number for the noise generation. Should be negative.

## `dispersion float`

1σ value of the background.

## `prec float`

Defines the precision for the calculation of the value of each pixel. A typical value is 0.1.

## `seeing int float`

`int = 0`: if false.  `int = 1`: if true.

If true, will convolve the image by a Gaussian filter with a full width at half maximum of size `float` expressed in arcseconds. 

Note: for good accuracy the pixel size of the image must be small compared to the seeing, a minimum of 2 pixels, but with 4 pixels as an optimum.

## `seeing_e int float1 float2 float3`

`int = 0` : if false.`int !=0`: if true.

If true, will convolve the image by an elliptical Gaussian filter with a full width at half maximum of sizes (expressed in arcseconds)  `float1` and `float2`, oriented at PA (=`float3`) degrees. 

## `psf int filename`

`int = 0` : if false. `int !=0`: if true.

If true, will convolve the image by a user-provided PSF fits image filename. The PSF provided should be centered on the image and the pixel scale should be identical to the image to convolve.

## `binning int1 int2`

`int1 = 0`: if false.`int1 = 1`: if true.

If true will **bin** the image by `int2` pixels.

Note: If the binning is set, it is performed just after the seeing and before adding noise. The aim is to better calculate the seeing when the sampling of final image is low. It is not used during optimisation process (`cleanset 2`).
