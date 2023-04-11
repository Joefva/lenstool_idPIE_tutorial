``idPIE`` profile description
==============================

.. _dPIE_summary:

``dPIE`` summary
-----------------

A summary on the **dual Pseudo-Isothermal Elliptical** matter distribution (``dPIE``) may be found `here <https://projets.lam.fr/projects/lenstool/wiki/PIEMD>`_, and this type of gravitational potential is described at length in `Elìasdòttir et al. (2007, Appendix A) <https://ui.adsabs.harvard.edu/abs/2007arXiv0710.5636E/abstract>`_
. It is identified in ``lenstool`` by id: ``81``.

Assuming we neglect ellipticity in this documentation, ``dPIE`` profiles write:

.. math::

   \rho_{\mathrm{dPIE}}(r) = \frac{\rho_0}{\left[ 1 + \left( \frac{r}{s} \right)^2 \right] \left[ 1 + \left( \frac{r}{a} \right)^2 \right]}
   
where 
:math:`\rho_0` is the density normalisation, 
:math:`a` the core radius, and
:math:`s` the cut radius.

A sum of ``dPIE`` profiles may be assumed to represent the total matter density
:math:`\rho_m`
(baryons + dark matter) in the lens:

.. math::

   \rho_m = \sum_i \rho_{\mathrm{dPIE}, i}.

Thus the profile of the gravitational potential 
:math:`\Phi` may be deduced from the ``dPIE`` sum:

.. math::

   \Phi(r) = - 4 \pi G \sum_i \int_0^r \mathrm{d}s s^{-2} \int_0^s \mathrm{d}t t^2 \rho_{\mathrm{dPIE}, i}(r).

For one ``dPIE`` profile 
:math:`\rho_{\mathrm{dPIE}}(r)`, the potential writes:

.. math::

   \Phi_{\mathm{dPIE}}(r) = \frac{a^2 s^2}{a^2 - s^2} \left[ \frac{s}{r} \arctan \frac{r}{s} - \frac{a}{r} \arctan \frac{r}{a} + \frac{1}{2} \ln \left( \frac{r^2 + s^2}{r^2 + a^2} \right) \right].

If we assume the intra-cluster medium (ICM) to be in hydrostatic equilibrium, we may simplify the Navier-Stokes equation to:

.. math::

   \frac{\partial_r \left( n_e T_e \right)}{n_e} = \frac{\mu_g m_a}{k_B} \partial_r \Phi,
   
where
:math:`n_e` is the ICM electron number volume density, 
:math:`T_e` the ICM electron temperature, 
:math:`\mu_g \approx 0.60` the mean molecular weight of the ICM gas,
:math:`m_a \approx 1.66 \times 10^{-27}` kg the unified atomic mass, and
:math:`k_B` the Boltzmann constant.

Assuming the temperature
:math:`T_e` to be a function of the electronic density, we can integrate this expression to:

.. math::

   \mathcal{J}_z (n_e) = \int_0^{n_e} \mathrm{d} n \frac{n T_e (n)}{n} = \frac{\mu_g m_a}{k_B} \Phi (r),
   
where
:math:`\mathcal{J}_z` is a bijection, as long as the radial density profile 
:math:`\rho_m` is a sum of ``dPIE`` potentials. 
Using a self-similar polytropic temperature profile, the 
:math:`\mathcal{J}_z` integral only depends on redshift
:math:`z`.
Bijections being invertible functions, we may revert the previous equation, thus yielding the ``idPIE`` density profile:

.. math::

   n_e = \mathcal{J}^{-1}_z  \left( \frac{\mu_g m_a}{k_B} \Phi (r) \right).






