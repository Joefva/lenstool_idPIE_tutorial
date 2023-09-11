# PIEMD

Set the potential profile to the type dPIE described in [Eliasdottir et al. 2007](http://arxiv.org/abs/0710.5636).

In `set_lens.c:set_dynamics()`, the impact parameter is computed as such:

$$b_0 = \frac{6 \pi \sigma_0^2}{c^2}$$

with $\frac{\pi}{c^2} = 7.2 10^{-6}$ arcsec / $(\rm km/\rm s)^2$. To obtain this value, $\pi$ is converted to 648,000 arcsec.


In file `e_grad2.c`, the 2nd derivatives of the gradient are computed as such with the core radius $a$ and the cut radius $s$ in arcsec:

$$t05 = b_0 \frac{s}{s - a}$$

$$z = \sqrt{R^2 + a^2} - a - \sqrt{R^2 + s^2} +s$$

$$p = \left( 1 - \frac{1}{\sqrt{1 + \frac{R^2}{a^2}}} \right) \frac{a}{R^2} - \left( 1 - \frac{1}{\sqrt{1 + \frac{R^2}{s^2}}} \right) \frac{s}{R^2}$$

$$\partial^2_{xx} = b_0 \frac{s}{s - a} \left( p\frac{x^2}{R^2} + z \frac{y^2}{R^4} \right)$$

$$\partial^2_{yy} = b_0 \frac{s}{s - a} \left( p\frac{y^2}{R^2} + z \frac{x^2}{R^4} \right)$$

$$\partial^2_{xy} = b_0 \frac{s}{s - a} \left( p\frac{x\ y}{R^2} - z \frac{x\ y}{R^4} \right)$$

From the 2nd derivatives, the convergence is computed in `g_mass.c:computeKmass()`

$$\text{To fill the equation} -> why?$$

$$\Sigma(R) = \frac{\sigma_0^2}{2 G} \frac{s}{s -a} \left(\frac{1}{\sqrt{R^2 + a^2}} - \frac{1}{\sqrt{R^2 + s^2}} \right)$$

The theoretical expression taken from Eq. 7 in [Limousin et al. 2005](http://arxiv.org/abs/astro-ph/0405607) is

$$\Sigma(R) = \frac{\sigma_0^2}{2 G} \frac{s}{s -a} \left(\frac{1}{\sqrt{R^2 + a^2}} - \frac{1}{\sqrt{R^2 + s^2}} \right)$$


and the critical mass is 

$$\Sigma_{crit} = \frac{c^2}{4 \pi G} \frac{D_{OS}}{D_{OL} D_{LS}}$$

By taking the ratio with $\Sigma_0 = \frac{\sigma_0^2}{2G}$, we find 

$$\kappa_{th} = \frac{\Sigma_0}{\Sigma_{crit}} = \frac{2 \pi \sigma_0^2}{c^2} \frac{D_{OL} D_{LS}}{D_{OS}}$$

Therefore the relation between Lenstool and the theory is 

$$\kappa_{th} = \frac{2}{3}\ \kappa_{lt}$$

Which translates in velocity dispersion as

$$\sigma_{\rm 0\ th} = \sqrt{\frac{3}{2}}\ \sigma_{\rm 0\ lt}$$

Note that the  [mass]() keyword corrects for this factor internally, and returns the theoretical convergence map.

We give an instance of dPIE potential:
```
potential  1
        profil           81
        x_centre         0.
        y_centre         0.
        ellipticite      0.
        angle_pos        0.
	core_radius_kpc  100.
	cut_radius_kpc   1500.
	v_disp           1000.
        z_lens           0.2
        end
```
