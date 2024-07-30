ICM Temperature models
==========================

If no temperature map is provided, then it is necessary to provide a temperature model in order to compute the different ICM observables (X-ray surface brightness, SZ effect temperature contrast, etc.). For purely lensing, this is not necessary.

.. we should think of producing a temperature map using this, and of making it an independent keyword, out of X-ray or SZE sections

``Temp0`` is the pivot temperature model, eq. (17) in 
`Allingham 2024 <https://arxiv.org/abs/2309.07076>`_:
:math:`T_0(z) = T_{500,c} (z) T_{\rm ref}`.
It may be computed using routine ``predT``:

.. code-block:: console
	
	predT0 <redshift> <model_type> <M_500,c>
	
where the mass
:math:`M_{500,c}` is in
:math:`M_{\odot}`, and the ``<model_type>`` corresponds to the regression used for
:math:`P_e (n_e)`. By default, use ``polyEv1`` for the latter.

``Jz_array`` indicates how to compute the Jz function, relating the potential to the ICM density 
:math:`n_e`. 
It takes three arguments:

- An integer. ``0``: do not perform the computation. ``1``: perform it.

- A string for the model type. By default, use ``polyE``. Other option is ``polyA``, which should be more up-to-date.

- A second string for the name of the output array. If the array is not computed (``0``), this array must already exist.

The different temperature models are listed here:

- ``polyEv1``: uses the reduction of a polytropic temperature distribution, with a varying index. Reduction over 12 X-COP clusters. See parameters values in the table below.
- ``polyAv1``: uses the reduction of a polytropic temperature distribution, with a varying index. Reduction over 12 X-COP clusters, and 3 strong lensing clusters' *XMM-Newton* spectrocopic data.  See parameters values in the table below.

The polytropic index model writes:

.. math::

    T_e &= \eta_T T_{500,c} \left( \frac{n_e E(z)^{-2}}{\eta_n} \right)^{\Gamma (n_e) - 1},

where 
:math:`E(z) = H(z)/H_0` is the scaled Hubble factor at a cluster redshift
:math:`z`. 
Assuming the polytropic index 
:math:`\Gamma` to vary with the ICM density,

.. math::
    \Gamma (n_e) &= \Gamma_0 \left[ 1 + \Gamma_S \arctan \left( \ln \frac{n_e E(z)^{-2}}{\eta_n} \right) \right],
    
where

.. math::

   \eta_T = (1e6*3.426e-3/8.85)*(\eta_P/\eta_n).

We specify the parameters of different models in the table below.

.. table:: ICM Temperature model parameters
   :widths: 20 15 15 15 15

   +----------------+-----------------+-----------------------------------+-------------------+-----------------------+
   | Id             | :math:`\eta_P`  | :math:`\eta_n` [cm :math:`^{-3}`] | :math:`\Gamma_0`  | :math:`\Gamma_S`      |
   +================+=================+===================================+===================+=======================+
   |                |                 |                                   |                   |                       |
   +----------------+-----------------+-----------------------------------+-------------------+-----------------------+
   | ``polyEv1``    |                 |                                   |                   |                       |
   +----------------+-----------------+-----------------------------------+-------------------+-----------------------+
   | ``polyAv1``    |  4.61           |  :math:`1.54\times 10^{-3}`       | 1.02              | -0.15                 |
   +----------------+-----------------+-----------------------------------+-------------------+-----------------------+

