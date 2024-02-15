# Einasto potential (Work-in-progress)

Set the potential profile to the Einasto potential

In the parameter file, rhos is assumed in $10^{12}\ \rm{M}_\odot / \rm{kpc}^2$.

In `set_lens.c:set_dynamics()`, the impact parameter is computed as such:

$$b_0 = \frac{c H_0}{4\pi G}  \frac{1}{D_{OS}} \rho_s$$

The deflection angle is given by

$\theta_2 = \theta_s d(n)^{-n}$, with $d(n) = 3n-1/3 + 8/1215/n + 184/229635/n^2 + 1048/31000725/n^3 - 17557576/1242974068875/n^4$

$$\alpha(\theta) = \frac{b_0}{ 2 (2\pi)^{n-1} \sqrt{n} \Gamma(n)} (\frac{\theta}{\theta_2})^2 \ \rm{Tab2(n)}$$

This potential is tabulated with files `mat_2nplus1.txt`, `mat_2n.txt`, `mat_2nplus2.txt`. The code to build these tables is TBD

