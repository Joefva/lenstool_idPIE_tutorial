# Windows installation

## Compiling Lenstool

Cygwin is an open-source software package manager for Windows. You can install Lenstool with it and interact with DS9 in the same way as you would do on Linux or Mac OSX systems. More details can be found on the [Cygwin website](https://www.cygwin.com).

First, download and execute the setup program following instructions [here](https://www.cygwin.com/install.html). The default installation settings are recommended.

In order to compile Lenstool, you need to install the following packages: `libcfitsio-devel`, `libwcs-devel`, `libgsl-devel`, `gcc-core`, `make`, `m2-base`. It is also recommended to install the following packages for later usage: `vim`, `perl`.

Then, in a Cygwin Terminal, download and untar the lenstool tarball

```
curl -O https://git-cral.univ-lyon1.fr/lenstool/lenstool/-/archive/8.0.4/lenstool-8.0.4.tar.gz
tar xzf lenstool-8.0.4.tar.gz
cd lenstool-8.0.4
```

Finally, compile and install Lenstool. This can be very slow (>30min)

```
./configure --disable-shared --with-cfitsio-include-path=/usr/include/cfitsio --with-cfitsio-lib-path=/usr/lib --with-wcslib-include-path=/usr/include/wcslib --with-wcslib-lib-path=/usr/lib --with-gsl-include-path=/usr/include --with-gsl-lib-path=/usr/lib 
make
make install
```

You should be able to call the lenstool executable from anywhere

```
$ lenstool.exe
Unexpected number of arguments

USAGE:
lenstool  input_file [-n]
```

You can test lenstool with the parameter files and test data in the examples directory.

## Interacting with DS9

[DS9 SAOimage](https://sites.google.com/cfa.harvard.edu/saoimageds9/download) Windows 64bits version is the preferred graphical interface to interact with Lenstool. Interactions use of the XPA communication protocol. The XPA commands (e.g. xpaget, xpaset, etc) can be downloaded from [here](https://ds9.si.edu/download/cygwin64), and should be copied in the `C:/Cygwin64/bin` directory, or any place in the `$PATH`. 

Lenstool provides several Perl scripts to interact with DS9, for instance:

- `pcl` : plot the critical lines.
- `pelli`: plot catalogs of objects in Lenstool format (e.g. images, sources, cluster member galaxies) onto a DS9 image.
- `garc.pl`: retrieve ellipse regions from DS9 and convert them into a Lenstool catalog format.

## Troubleshooting

On Windows, it is possible that the Perl scripts do not find the DS9:ds9 XPA template (although DS9 says it is connected). In this case, run the command

```
$ xpaget xpans
DS9 ds9 gs 7f000001:56819 localhost
```

and set the Lenstool DS9 environment variable to
```
export DS9=localhost:56819
```
