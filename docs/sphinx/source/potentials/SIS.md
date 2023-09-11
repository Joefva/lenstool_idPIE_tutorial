# SIE

Set the potential profile to the type SIE.

In `set_lens.c:set_dynamics()`, the impact parameter is computed as such:

$$b_0 = \frac{4 \pi \sigma_0^2}{c^2} \frac{D_{LS}}{D_{OS}}$$

with $\frac{\pi}{c^2} = 7.2 10^{-6}$ arcsec / (km/s)^2. To obtain this value, $\pi$ is converted to 648,000 arcsec.

The ellipticity of the potential ε is proportional to the ellipticity of the mass distribution 
$e_{mass}$

$$\epsilon = e_{mass} / 3$$

Circular SIS has $\epsilon = 0$.

A circularised radius is defined as $R^2 = (1 - \epsilon)x^2 + (1+\epsilon)y^2$.

The projected effective lensing potential in direction $\boldsymbol{\theta}$ of Newtonian potential $\Phi$ is

$$\psi (\boldsymbol{\theta}) \approx \frac{2}{c^2} \frac{D_{LS}}{D_{L} D_{S}} \int_0^{D_{LS}} \mathrm{d}\chi \Phi(\boldsymbol{\theta} D_A(\chi); \chi)$$

where $D_A$ is the angular diameter distance.
The SIE lensing potential writes

$$\psi (x, y) = b_0 R$$

Program `e_grad.c` computes the first derivatives of this potential

$$\partial_{x} \psi = \frac{b_0 (1 - \epsilon)}{R}  x$$

$$\partial_{y} \psi = \frac{b_0 (1 + \epsilon)}{R}  y$$

In file `e_grad2.c`, the 2nd derivatives of the gradient are computed in 2D in the amplification frame, and rotated afterwards back to the reference frame. 

The second derivatives of the lensing potential are

$$\partial^2_{xx} \psi = \frac{b_0 (1 - \epsilon^2)}{R^3}  y^2$$

$$\partial^2_{yy} \psi = \frac{b_0 (1 - \epsilon^2)}{R^3} x^2$$

$$\partial^2_{xy} \psi = - \frac{b_0 (1-\epsilon^2)}{R^3} xy$$

From the 2nd derivatives, the convergence is computed in `g_mass.c:computeKmass()`. 

$$\kappa = \frac{1}{2} (\partial^2_{xx} + \partial^2_{yy}) \psi = \frac{b_0(1-\epsilon^2)}{2R^3}(x^2+y^2)$$

The shear is computed in `g_shear.c`. 

$$\gamma_1 = \frac{1}{2} (\partial^2_{xx} - \partial^2_{yy}) \psi = \frac{b_0(1-\epsilon^2)}{2R^3} ( y^2 - x^2)$$

$$\gamma_2 = - \partial^2_{xy} \psi = \frac{b_0(1-\epsilon^2)}{R^3} xy$$

$$\gamma = \sqrt{\gamma_1^2 + \gamma_2^2} = \frac{b_0(1-\epsilon^2)}{2R^3} (x^2 + y^2)$$
