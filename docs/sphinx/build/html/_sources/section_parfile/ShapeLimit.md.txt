# `shapelimit`


Under this identifier are defined the priors on the parameters that define a source shape.




## `s_center_x int float1 float2 float3`

Range of position along the X axis for the center of the source in arcsec. The reference point for this range is the barycenter of sources is attached to a system of multiple images, or the reference point defined in the .par file if not.


## `s_center_y int float1 float2 float3`

Range of position along the Y axis for the center of the source in arcsec. The reference point for this range is the barycenter of sources is attached to a system of multiple images, or the reference point defined in the .par file if not.


## `s_sig_x int float1 float2 float3`

Range on the size of the major axis in arcsec


## `s_sig_y int float1 float2 float3`

Range on the size of the minor axis in arcsec


## `s_angle int float1 float2 float3`

Range on the orientation of the ellipse defining the source. The angle is defined anti-clockwise from west to north axis.


## `s_mag int float1 float2 float3`

Range on the unlensed magnitude of the source


## `index int float1 float2 float3`

Range on the value of the Sersic index $n$ for sources modeled with Sersic profile.


