Potfile
=========

.. _potfile:

Use ``potfile`` keyword for file of potentials optimised together (following a scaling relationship).
---------------------------------------------------------------------------------------------------------

.. To use ``idPIE`` profiles, one must choose which ``dPIE`` profiles are considered to trace the X-ray signal.
.. The ``idPIE`` profiles use the same parameters as the ``dPIE`` profiles, but convert them into their corresponding hydrostatic ICM density, and computes the expected X-ray signal. The joint optimisation of selected profiles yields additional constraints.
.. In practice, ``dPIE`` profiles (id:``81``) are co-optimised with X-ray using ``idPIE`` profiles if keyword ``X-ray   2`` is added to the profile script.

For instance:

.. code-block:: console

	potfile 1
		filein        9 potfile.cat
		zlens         0.3
		type          81
		mag0          20.
		corekpc       0.15
		sigma         3 190. 5.
		cutkpc        3 10. 3.
		slope_FJ      3 1. 0.1
		Zero_point_FP 3 -0.6 0.03
		slope_SB      3 0.30 0.02
		Factor_Re     3 2. 0.35
		vdscatter     0 0. 0.
		rcutscatter   0 0. 0.
		pivot_sigma   2.
		pivot_mu      20.
		end



