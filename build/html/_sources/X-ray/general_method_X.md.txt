# X-ray extension: Basics

Since the work of [Beauchesne+23](https://ui.adsabs.harvard.edu/abs/2023arXiv230110907B/abstract), Lenstool is able to use X-ray data to model the intra-cluster gas. It only requires to define a new section in the parameter file that will define the X-ray observation and needs to be activated per potential with a simple keyword.

## How it works

To make it simple, the X-ray extension bring the ability of Lenstool to compute the $\int n_e n_p dl$ for a potential which allow to constraint the shape of the gas haloes with the count map and to also produce the related quantities as map. For now, only the dPIE are implemented and thus, we will focus on this potential to detail how it has been put in place.

### dPIE

The analytical formulae associé au dPIE and that is unique to each potential is the computation of $\int \rho^2 dl$. We use the
equation presented in [Bonamigo+17](https://ui.adsabs.harvard.edu/abs/2017ApJ...842..132B/abstract) and to define their elliptical counter part we use the same transformation as in [Elıasdottir+07](https://arxiv.org/abs/0710.5636). As we are considering the sum of multiple potential there is two different interesting formulae. If we consider the $i^{th}$ and $j^{th}$ potentials, we have to compute $\int \rho_i^2 dl$ and $\int \rho_i \rho_j dl$ that are presented in equation 5 and 7 in [Bonamigo+17](https://ui.adsabs.harvard.edu/abs/2017ApJ...842..132B/abstract). As we can see, these expressions only depends of the usual dPIE parameters. However, each of these potential does not have to only consist of gas, thus a gas fraction has to be defined for these X-ray activated potentials, which bring one more parameter to the potential. By default the gas fraction is fixed to one and it is the current recommended practice as it implies no assumption on the gas following the DM distribution. The gas fraction behave like any other potential parameter and can be optimised between 0 and 1.

The definition of a dPIE potential is then almost the same as without the X-ray extension and is the following:

```
potential O6
    profile       81
    x_centre     -22.867836
    y_centre     17.190451
    ellipticity     0.133194
    angle_pos       -27.937929
    core_radius_kpc     153.952651
    cut_radius_kpc     1250.000000
    v_disp     338.723340
    X-ray     1
    Gas_fraction     1.000000
    z_lens     0.3475
    end
```

As we can see there is only `X-ray` and `Gas_fraction`, the first being a boolean and can be set to 0 or 1 and the second is the previously discussed parameter. If other potential have to be implemented, they will follow the same pattern and just these two keywords will have to be added. The only exception is potentials that will follows some specific assumptions.

### Plasma emission model

The model is separated in two parts, the hard coded and the user provided. The earlier is only the transformation from $\rho^2$ to $n_e n_p$ while the later is the final transformation from $\int n_e n_p dl$ to the actual number of counts. The transformation of the mass to the proton and neutron density is the following:

$$
\rho=\mu(n_e+n_p)



$$

$$
\Rightarrow n_e n_p=\frac{\rho^2}{\mu^2 \left(1+{\rm nhc}\right)\left(1+\frac{1}{\rm nhc}\right)}



$$

Where $\mu$ and ${\rm nhc}$ are the mean molecular weight per particle in a fully ionised gas and the conversion factor from $n_p$ to $n_e$, respectively. For now, we hardcoded the value of this two parameters to the following work of [Asplund+09](https://ui.adsabs.harvard.edu/abs/2009ARA%26A..47..481A/abstract). Here are their values:
$\mu=0.5994$ and $nhc=\frac{1}{0.8527}$

Regarding the user provided part, it comes with the set up of the optimisation constraint in the new X-ray section of the parameter file. Indeed, the factor that transform $\int n_e n_p dl$ to the photon count have to be provided in the form of a map, the earlier integral being given in $cm^{-5}$. This map represent the plasma emission model time the exposure map and if we consider Chandra data, it can be obtained with the following procedure:

- Create an exposure map in $cm^2 s \,count / photon$ with merge_obs for example. [See here.](https://cxc.cfa.harvard.edu/ciao/ahelp/merge_obs.html)
- Compute a the emission for your emission model in $photon/cm^2/s$ with calc\_photon\_flux. [See here.](https://cxc.harvard.edu/sherpa/ahelp/calc_photon_flux.html)
- Normalize the emission from your model to a unitary emission in term of the mass of the gas. For an [APEC](https://heasarc.gsfc.nasa.gov/xanadu/xspec/manual/XSmodelApec.html) model, this is equivalent to choosing the right norm (${10^{-14}\over{4\pi[D_A(1+z)]^2}}\int n_e n_HdV$ for $\int n_e n_p dl=1$). Using the following value:
    - $\frac{1}{(4. \times (1. + z)^2 \times (180.\times 60.) ^2 / \pi / 1e-14 )}$ and setting `pixel_area` keyword to the pixel area of your exposure map in arcmin. These two things will perform the normalization correctly.
        Notably, the exposure map produced by data reduction pipelines of other X-ray observatory may be different as for XMM-Newton for example, where the map does not take into account the pixel size in $cm^2$. We thus take into account this differences by offering a keyword `Chandra` to be set to $0$ if the pixel size is not in th exposure map.

We will now move to the optimisation section where we will continue on explaining the keyword of the `X-ray` and finally summarize them with the presentation of a complete section.

## Optimisation

The optimisation is performed through a Monte Carlo method, with the Markov Chains Monte Carlo engine [bayeSys](https://www.inference.org.uk/bayesys/) implemented in the lenstool C code or through any optimiser with the Python wrapper of the Lenstool C library. Thus, it needs a loglikelihood which can be choose between a Poisson loglikelihood and a Poisson-gamma mixture loglikelihood. The earlier $\mathcal{L}_{\rm Poisson}$ does not take into account an intrinsic errors due to the assumption of the modelling method in contrary to the latter $\mathcal{L}_{\rm PG}$. They are defined as follow:

$$
\mathcal{L}_{\rm Poisson}=\sum_{i} D_i\log\left(M_i\right)-M_i-\log\left(D_i!\right)

$$

$$
\mathcal{L}_{\rm PG}=\sum_i \log\left(\frac{\Gamma\left(D_i+\frac{M_i^2}{\sigma_{\rm X}^2}\right)}{D_i!\Gamma\left(\frac{M_i^2}{\sigma_{\rm X}^2}\right)}\left(\frac{M_i}{M_i+\sigma_{\rm X}^2}\right)^\frac{M_i^2}{\sigma_{\rm X}^2}\left(\frac{\sigma_{\rm X}^2}{\mu_i+\sigma_{\rm X}^2}\right)^{D_i}\right)

$$

Where $D_i$ and $M_i$ and $\sigma_{\rm X}$ are the observed and the model count number in the $i^{th}$ bin. $\sigma_{\rm X}$ is the systematic uncertainty due to the method which can also be defined per bin. The computation of these likelihood will be automatically done is the `X-ray` section of the parameter file is properly defined (i.e. the plasma emission model) and set up for an optimisation. Such section looks like the following:

```
X-ray
   pixel_area 0.00107584
   Chandra 1
   Optimization 1
   Optimization_z 0.3475
   bkg_map 3 S1063_bkg_map_fit.fits
   count_map 3 S1063_count_map_fit.fits
   count_factor_map 3 S1063_count_factor_map_fit.fits
   intrinsic_error 1.0 1 0.01 1.0
   end
```

`Chandra` and `pixel_area` have been defined in the previous section. `bkg_map` and `count_map` are the background and observed count map. The former is added the initial count model while the latter refers to the data that we want to fit. The `count_factor_map` is the map detailed in the previous section that make the link between $\int n_e n_p dl$ and the photon count. We thus have three more keywords to set up the optimisation, with in first `optimisation` which can be 0 or 1 and represent a boolean to activate the computation of the likelihood. `optimisation_z` is the redshift of the gas modelled. Finally, `intrinsic_error` represent the systematic error and has the same syntax as an optimised parameter in the `potfile` section. The first floating value define its value, if its 0 a poisson likelihood will be computed if not the other if it is fixed. The following integer and floating values are defining the optimisation behavior and are the following:

- `0 0.01 1.0` : First integer set to 0 means no optimisation and the two other values are ignored.
- `1 min max` : Optimisation with a uniform prior, with the bound defined as here.
- `3 mean std` : Optimisation with a gaussian prior.

Once that section has been defined, the model can be optimised by the MCMC engine included in C code which is bayeSys or any other optimiser/sampler through the python interface. There are example of how to use these other methods in the directory `perl` in the lenstool directory. See the following files :
- `dynamic_nested_sampler.py` : Example with `Ultranest` and `Dynesty` with the creation of the normal output files of lenstool
- `pool_emcee_EnsembleSampler.py` : Example with `Emcee` with the creation of the `bayes.dat` and `burnin.dat` solely.

At the end of the optimisation or at the production of a `chires.dat` file, the code will generate the three following maps:
- `Xray_model_counts.fits`: Maps that has the same size has the imput maps and contains in each pixel the value of the best-fit count model.
- `Xray_residual_counts.fits` : Same as before, but with the residual (i.e. Data-model)
- `Xray_loglikelihood_pix.fits` : Same as before, but each pixel contains the value of the loglikelihood associated.

These allows you to see the best-fit count model and see which part of the field are badly/betterly reproduced. These map can be created for other models than the best as long as you have a parameter file for them by using the usual lenstool method to produce map, which is by specifying them in the `runmode` section with the following lines:
- `X-ray 2 0 z_lens Xray_model_counts.fits`
- `X-ray 3 0 z_lens Xray_residual_counts.fits` 
- `X-ray 4 0 z_lens Xray_loglikelihood_pix.fits`

These lines have to be used one by one, as lenstool does not have the hability to create multiple maps of the same keywords at the same time. Here, the size of the maps are defined by the input maps, so the integer related to the number of pixel per row and column is `0`.

In addition, other quantity related to the best-fit model can be found in the `chires.dat`  that contains will contains the usual lines associated with the other likelihood defined such as the lensing one. Here is an example of the X-ray lines:

```
chi X-ray surface brightness
N_pixel    16900
Cash_Statistic    -437152.56002
Cstat    4661.77537
log(likelihood)    -33189.73608
Monte Carlo estimation of the quality of the fit: Mean: -32915.46507 Std: 87.35700
Interval 1 sigma: min -> -33002.06100 ||max -> -32829.06987 
Interval 3 sigma: min -> -33177.52215 ||max -> -32648.07052 
Interval 5 sigma: min -> -33255.71946 ||max -> -32599.59211
```


Where `N_pixel` contains the total number of pixel, the  `Cash_Statistic` is equal to $-2\times\log\left(\mathcal{L}\right)$ (Correct definition if $\sigma_{X}=0$). The `Cstat` is defined as follows:
$\text{Cstat}=\sum^{\rm N_{pixel} }_{\rm i} 2(M_i-D_i+D_i\log\left(\frac{D_i}{M_i}\right))$
It is similar to the one implemented in Xspec or Sherpa. In case $M_i=0$, we replace the previous term in the sum by $2 D_i$. We added these two other likelihoods to provide a comparison with other X-ray fitting software. These lines also contains the results of the goodness of fit procedure presented in [Beauchesne+23](https://ui.adsabs.harvard.edu/abs/2023arXiv230110907B/abstract). The idea of this procedure is to see if the observed data are likely to be produced by the count model, ideally we would build such distribution by using the full posterior however for computing time reason we only use the best-fit model. Hence, we are sampling in each pixels $100000$ realisation of the associated distribution which is a Poisson distribution or the Poisson-Gamma mixture. The number of counts in the pixel is the mean of the Poisson distribution for the earlier when it is the mean of the Gamma distribution in the latter. This distribution have $\sigma_{X}$ as standard deviation and the random variate defined is then the mean of the Poisson distribution of the mixture. We then compute the likelihood associated with each of the sample and extract the following information:
```
Monte Carlo estimation of the quality of the fit: Mean: Sample mean Std: Sample standard deviation
Interval 1 sigma: min -> percentile 16% ||max -> percentile 84% 
Interval 3 sigma: min -> percentile .135% ||max -> percentile 99.865% 
Interval 5 sigma: min -> percentile .0000286% ||max -> percentile 99.9999713%
```

From this information, you can see how likely the model will produce the observed data and set up a threshold for your own analysis and see how much you should complexify your model. To make an analogy with a gaussian likelihood, this criteria is computing an equivalent to the $\chi^2\sim1$ which does not exist for Poisson-like likelihood. Indeed,  the value would be changing for each different case.


## Data product implemented

For now, there are not much maps that can be produced by more will come as the extension is used. To create a map, here is the syntax to add in the `runmode`:
```
runmode
    X-ray type N_pix z name_file
    end
```
`type` (integer) is the type of map that you can produce, `N_pix` the number of pixel per column and row, `z` the redshift for which you would like to compute the map (that plane need to have some X-ray potential to not return only $0$) and finally the name of the fits file you want to create. Here are the type of map you can do:
-	$0$: Do nothing
-	$1$: Map of the mass model ($\int \rho_{gas}^2$) times the map provided through the `Emissivity_map` keyword in the `X-ray` section. If the cooling function is provided, you will obtain the surface brightness. It can be used to create a count map by providing the `count_factor_map` in the previous keyword, the difference with `type` $2$ is that the map is interpolated to be computed at the defined resolution with a bilinear interpolation. 
-	$2$: Count model with the same size as the input data map
-	$3$: residual map with the same size as the input data map
-	$4$: Loglikelihood map with the same size as the input data map

Type of maps to be implemented in the future:
-	Map of the projected gas mass
-	Map of the projected gas fraction
-	...

If the type of map that you would like to see is not implemented, you can contact us to see if we can put that in place.

## Chandra data reduction and processing wrapper



## Developement

