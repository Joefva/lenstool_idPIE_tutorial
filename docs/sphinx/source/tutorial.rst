Tutorial
=========

.. _idPIE_tutorial:

Use ``idPIE`` X-ray profiles.
-----------------------------

To use ``idPIE`` profiles, one must choose which ``dPIE`` profiles are considered to trace the X-ray signal.
The ``idPIE`` profiles use the same parameters as the ``dPIE`` profiles, but convert them into their corresponding hydrostatic ICM density, and computes the expected X-ray signal. The joint optimisation of selected profiles yields additional constraints.
In practice, ``dPIE`` profiles (id:``81``) are co-optimised with X-ray using ``idPIE`` profiles if keyword ``X-ray   2`` is added to the profile script.

For instance:

.. code-block:: console

	potential O1
		profile          81
		X-ray	         2
		x_centre         0.
		y_centre         0.
		ellipticity      0.5
		angle_pos        0.
		core_radius_kpc  100
		cut_radius_kpc   2500.
		v_disp           1000.
		z_lens           0.3
		end
	limit O1
		x_centre         1 -10. 5. 0.01
		cut_radius_kpc   1 500. 10000. 100.
		end



