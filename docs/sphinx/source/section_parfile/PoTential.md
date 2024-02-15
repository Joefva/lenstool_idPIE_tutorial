<<<<<<< HEAD
# potential



## profile int

Set the type of profile. You can find the list of potentials.

## x\_centre float
=======
# `potential`



## `profile int`

Set the type of profile. You can find the list of potentials [here](../Supported_pot.rst).

## `x_centre float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Set the x position of the center $x_c$. In arcseconds.


<<<<<<< HEAD
## y\_centre float
=======
## `y_centre float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Set the y position of the center $y_c$. In arcseconds.


<<<<<<< HEAD
## x\_centre\_wcs float
=======
## `x_centre_wcs float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Same as `x_centre` but gives the position is degree WCS. This keyword
needs the presence of the [`reference`]() keyword in the [`runmode`]() Section.


<<<<<<< HEAD
## y\_centre\_wcs float
=======
## `y_centre_wcs float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Same as `y_centre` but gives the position is degree WCS. This keyword
needs the presence of the [`reference`]() keyword in the [`runmode`]() Section.


<<<<<<< HEAD
## masse float
=======
## `masse float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Set the point mass $M_0$ expressed in $10^{12}$ solar masses. For the NFW profile, this parameter corresponds to $M_{200}$ and is in Solar Mass unit.


<<<<<<< HEAD
## pmass float
=======
## `pmass float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Set the mass per surface unit, expressed in ${\rm g.cm^{-2}}$.


<<<<<<< HEAD
## ellipticite float
=======
## `ellipticite float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Set the ellipticity  of the mass distribution.


<<<<<<< HEAD
## ellip\_pot float
=======
## `ellip_pot float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Set the ellipticity of the potential distribution.


<<<<<<< HEAD
## angle\_pos float
=======
## `angle_pos float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Set the position angle of the potential distribution expressed in degree (90° relative to PA). It corresponds to the direction of the semi-major axis of the iso-potential counted from the horizontal axis, counterclockwise.


<<<<<<< HEAD
## core\_radius float
=======
## `core_radius float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Set the core radius $r_0$, expressed in arcseconds.


<<<<<<< HEAD
## cut\_radius float
=======
## `cut_radius float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Set the cut radius $r_c$, expressed in arcseconds.


<<<<<<< HEAD
## v\_disp float
=======
## `v_disp float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Set the central velocity dispersion σ0 of the 3D velocity field (supposed isotropic). Expressed in kms. The relation between `v_disp` and the observed line-of-sight velocity dispersion depends on the mass profile (see Wu 1993, ApJ, 411, 413) and the anisotropy factor.  For isothermal mass profiles, the observed line-of-sight velocity dispersion is generally obtained from the central galaxies of the cluster and is more or less σlos(0). The correcting factor is therefore negligeable. However, for other profile (non isothermal), you have to compute by yourself the correction.
The correction is calculated for approximate King profile in Kneib 1993 (eq. 3.63). 

Caution: in case of potential PIEMD, the parameter `v_disp` is not the true velocity dispersion (see PIEMD).

<<<<<<< HEAD
## exponent float
=======
## `exponent float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Set the exponent of the slope α of the potential distribution. Isothermal=0.5.


<<<<<<< HEAD
## alpha float
=======
## `alpha float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Same as exponent.


<<<<<<< HEAD
## beta float
=======
## `beta float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Set the exponent of the slope β of the elliptical part of the potential distribution. 


<<<<<<< HEAD
## z\_lens float
=======
## `z_lens float`
>>>>>>> e8bc58d1858b26df7c5823c468ad671bf631e9ed

Set the redshift of the clumps. At present, all the clump must be at the same redshift.
