# External maps

Set the potential profile to the type external maps

This potential takes parameters as `parameter int filename`

`parameter` can take the following values:
`kappamap`: a convergence map
`gamma1map`: a shear map (x-axis projection)
`gamma2map`: a shear map (y-axis projection)
`dplxmap`: a displacement map along the x direction.
`dplymap`: a displacement map along the y direction.
`potenmap`: a potential map 

All maps should be provided as FITS format (`filename`), have the same WCS, and be normalised at DLS/DS=1 (apart from potenmap).

`int`: only read maps if non-zero. Value should be 3 for usual WCS formats (RA---TAN / DEC--TAN).


In addition the redshift of the plane is provided by the `z_lens` parameter.

