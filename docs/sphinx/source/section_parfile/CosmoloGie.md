# `Cosmologie`



## `Model`
Can be `1`, `2`, `3`, or `4`. Default value is `Model = 1`.
- `1`  for CPL model
- `2`  for Cardassian model
- `3`  for Interacting DE Model
- `4`  for Holographic Ricci Scale with CPL


## `H0 float`
float defines the value of $H_0$ in Mpc/km/s. Default value is $H_0 = 50$.


## `omega float`
float defines the value of $\Omega_{0}$. Default value is  $\Omega_{0} = 1$.

## `lambda (or omegaX) float`
float defines the normalized value of $\lambda$. (for a flat universe  $\Omega_{0} +  \lambda = 1.$)
Default value  $\lambda = 0$.

## `omegaK float`
float defines the normalized value of the curvature of the Universe  $\Omega_k$

## `wX (q, or w0) float`
If Model is equal to 1, float defines the first parameter in the CPL model.
If Model is equal to 2, float defines the $q$ parameter in the Cardassian model.
If Model is equal to 3, float defines the $w_x$ parameter in the Interacting DE model.
If Model is equal to 4, float defines the $w_0$ parameter in the Holographic Ricci scale with CPL.

## `wa (n, delta, or w1) float`
If Model is equal to 1, float defines the second parameter in the CPL model.
If Model is equal to 2, float defines the $n$ parameter in the Cardassian model.
If Model is equal to 3, float defines the $\delta$ parameter in the Interacting DE model.
If Model is equal to 4, float defines the $w_1$ parameter in the Holographic Ricci scale with CPL.


## Additional remarks on the Cosmologie identifier


### Model 1
Using the so-called CPL parameterization

$$w(z)=w_x+\frac{w_az}{1+z}$$,

proposed by Chevalier & Polarski (2001) and Linder (2003), the square of the Hubble parameter (normalized by $H_0$) can be written as


$$\frac{H(z)^2}{H_0^2}=(\Omega_k(1+z)^2+\Omega_r(1+z)^4+\Omega_0(1+z)^3)+(1-\Omega_k-\Omega_r-\Omega_0)(1+z)^{3(1+w_x+w_a)}exp(\frac{-3w_az}{1+z})$$


Certainly, in the code $\Omega_r \equiv 0$, always.


### Model 2
The modiﬁed polytropic Cardassian Universe (see [Gondolo & Freese, 2003]()) is a generalization of the original Cardassian model of [Freese & Lewis (2002)](). In such Universe the Hubble parameter is given by:

$$\frac{H(z)^2}{H_0^2}=\Omega_k(1+z)^2+\Omega_r(1+z)^4+\Omega_0(1+z)^3\left[1+((\frac{1-\Omega_k-\Omega_r}{\Omega_0})^{q}-1)(1+z)^{3q(n-1)}\right]^{1/q}$$ 


### Model 3
In the interacting Dark Energy model (Citation needed!) we have

$$\frac{H(z)^2}{H_0^2}=\Omega_k(1+z)^2+\Omega_r(1+z)^4+(1-\Omega_k-\Omega_r-\Omega_0)(1+z)^{3(1+w_x)}+\frac{\Omega_0}{\delta+3w_x}\left[\delta(1+z)^{3(1+w_x)}+3w_x(1+z)^{3-\delta}\right]$$ 


### Model 4
Holographic Ricci Scale with CPL (Citation needed!):

$$\frac{H(z)}{H_0}=(1+z)^{\frac{3}{2}\frac{1+r_0+w_0+4w_1}{1+r_0+3w_1}}\left[\frac{1+r_0+3w_1z/(1+z)}{1+r_0}\right]^{-\frac{1}{2}\frac{1+r_0-3w_0}{1+r_0+3w_1}}$$

In this case,

$$w(z)=w_0+\frac{w_1z}{1+z}$$

and

$$r_0=\frac{\Omega_0}{1-\Omega_0}$$ 
