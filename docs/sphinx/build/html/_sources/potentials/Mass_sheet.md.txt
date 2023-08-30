# Mass sheet

In `set_lens.c:set_dynamics()`, the impact parameter is computed as such:

$$b_0 = \frac{1}{2} \frac{\Sigma_0}{\Sigma_{\rm crit}}$$

with $\Sigma_0$ in $\rm g/cm^2$, and $\Sigma_{\rm crit} = \frac{c^2}{4 \pi G}\frac{D_{\rm OS}}{D_{\rm OL} D_{\rm LS}} \,{\rm g/cm^2}$. 

Note that the factor $1/2$ makes the estimated density to be half the true value.

In file `e_grad2.c`, the 2nd derivatives of the potential are computed as such:

$\partial_{xx} \phi = \partial_{yy} \phi = b_0$

$\partial_{xy} \phi = \partial_{yx} \phi = 0$


In file `e_grad.c`, the 1st derivates of the potential are computed as such:

$\partial_x \phi = b_0 (x_{\rm img} -x_{\rm lens})$

$\partial_y \phi = b_0 (y_{\rm img} -y_{\rm lens}) $

This profile is not well tested.
