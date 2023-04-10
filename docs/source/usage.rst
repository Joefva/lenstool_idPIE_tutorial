``idPIE`` profile description
==============================

.. _dPIE_summary:

``dPIE`` summary
-----------------

A summary on the **dual Pseudo-Isothermal Elliptical** matter distribution (``dPIE``) may be found `here <https://projets.lam.fr/projects/lenstool/wiki/PIEMD>`_, and this type of gravitational potential is described at length in `Elìasdòttir et al. (2007, Appendix A) <https://ui.adsabs.harvard.edu/abs/2007arXiv0710.5636E/abstract>`_
. It is identified in ``lenstool`` by id: ``81``.

Assuming we neglect ellipticity in this documentation, ``dPIE`` profiles write:

.. math::

   \rho(r) = \frac{\rho_0}{\left[ 1 + \left( \frac{r}{s} \right)^2 \right] \left[ 1 + \left( \frac{r}{a} \right)^2 \right]}
   
where 
:math:`\rho_0` is the density normalisation, 

