# shapemodel


Under this identifier are defined the parameters that define a source shape.




## s\_center\_x float

Position along the X axis for the center of the source in arcsec. The reference point for this range is the barycenter of sources is attached to a system of multiple images, or the reference point defined in the .par file if not.

## s\_center\_y float

Position along the Y axis for the center of the source in arcsec. The reference point for this range is the barycenter of sources is attached to a system of multiple images, or the reference point defined in the .par file if not.


## s\_sigx float

Value of the size of the major axis in arcsec


## s\_sigy float

Value of the size of the minor axis in arcsec


## s\_angle float

Value of the orientation of the ellipse defining the source. The angle is defined anti-clockwise from west to north axis.


## s\_mag float

Value of theunlensed magnitude of the source


## index float

Value of the Sersic index $n$ for sources modeled with Sersic profile.

## z float

Redshift of the source.

## id string

Identifier of the source.

## type int

Surface brightness density type
- 1: Velocity field $I(r)=sign(y)$ $I_0$ $\sqrt{|y|}$
- 2: Exponential disk  $I(r)=I_0$ $\exp(-r)$
- 3: 2D Gaussian $I(r)=I_g$ $\exp(-0.5\,r^2)$
- 4: Sersic $I(r)=I_0$ $\exp(-r^{1/n})$
- 5: Uniform disk within radius $I(r)=I_0$ for $r<a\ b$

with $I_0=10^{-0.4\,({\rm s_{mag}}-26)}$ and $I_g = 10^{-0.4\,({\rm s_{mag}}+48.57)+29}$
