# Lenstool FAQ

## Does the organization of the potentials in the _.par_ file matter?

Yes. Internally in Lenstool, the potentials are all saved into a large array or pointers. Here is the assumed order in the _lens[]_ array
   
```
             Indiv. optim. pot. | Fixed pot. |Potfile 0 | Potfile 1 | Accelerated pot. |
             ^                  ^            ^          ^           ^                  ^
             0              G.no_lens    G.nplens[0]  G.nplens[1]  G.nmsgrid         G.nlens
         
```

The _G_ structure contains a set of indexes that mark each section in the `lens[]` array. During processing, each section might be processed differently according on its particular type. Some indexes are set by the user 

 |**Internal name**|**Name in the _.par file**|**Description**|
 |-----------------|---------------------------|---------------|
 | G.no_lens       | grille / nlens_opt         | End of the individually optimized potentials with _limit_ section |
 | G.nmsgrid       | grille / nmsgrid            | Beginning of the potentials optimized with the multiscale grid method (no _limit_ section) |
 | G.nlens           | grille / n_lentille        | Total number of potentials (reset automatically by Lenstool if too large) |

The potfile indexes saved in the array `nplens[]` for the different potfiles are set automatically, according to the number of galaxies in each potfile. They mark the beginning of the potfile sections.

## How can I speed up the calculations? 

The optimization of the potfile can severly slows down the calculations, because Lenstool will compute the derivatives of the potential of all the potfile galaxies. If it happens that you already have an approximative idea of the potfile values, you can fix the "sigma" and "cutkpc" parameters. This will significantly speed up the calculations.

However, note that if you also optimize the redshift of the multiple images or the cosmological parameters, you will necessarily have to recompute the potfile.

## In Ubuntu, I get a compilation error with Lenstool version 6.8

The error message contains many missing math functions (log, pow, sin, etc). 

The solution is to type the gcc command line by hand, moving the "-lm" option to the end of the command line.

```
gcc  -g -O2 -fopenmp -lcfitsio -o lenstool_tab e_nfwg.o lenstool_tab.o midpnt.o nrutil.o polint.o qromo.o read_bin.o  -lm
```

## How can I interact with DS9?

Lenstool package contains scripts to display regions in DS9, using the [XPA binaries](http://ds9.si.edu/site/XPA.html).

You can download the executables and install them anywhere. In your .bashrc, you then need to add them to the PATH

For bash shell (to know your shell, you can type `echo $SHELL`),

```
export  PATH=$PATH:<your path to the xpa binaries>
```

For csh shell,
```
setenv PATH $PATH:<your path to the xpa binaries>
```
Once, you restart your shell, you should be able to open an image with DS9
```
ds9 my_image.fits
```
and display a Lenstool catalog of images
```
pelli image_wcs.cat
```
