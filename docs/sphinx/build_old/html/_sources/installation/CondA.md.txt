# Conda installation

Starting with Lenstool version 8, you can install lenstool including the new Python wrapper in a conda environment. 

First, create a conda environment named lenstool. You can skip this step if you want to install Lenstool in the default `base` environment. 

```
conda create -n lenstool
conda activate lenstool
```

Now you can download and untar the release-8 version of Lenstool

```
curl -O https://git-cral.univ-lyon1.fr/lenstool/lenstool/-/archive/8.0.4/lenstool-8.0.4.tar.gz
tar xzf lenstool-8.0.4.tar.gz
cd lenstool-8.0.4
```

To compile lenstool, you need to install the dependencies in your conda environment

```
conda install wcslib cfitsio gsl pip numpy <your compiler>
```

replacing `<your compiler>` with one of the following package name

* clang-osx-64 for Mac OSX
* gcc_linux-64 for Linux

More options can be found on the [Anaconda compiler web page](https://docs.conda.io/projects/conda-build/en/stable/resources/compiler-tools.html#compiler-packages.)

Finally, you can compile and install Lenstool

```
./configure --prefix=$CONDA_PREFIX --with-cfitsio-prefix=$CONDA_PREFIX --with-wcslib-include-path=$CONDA_PREFIX/include/wcslib --with-wcslib-lib-path=$CONDA_PREFIX/lib --with-gsl-prefix=$CONDA_PREFIX
make
make install
```

To install the Python wrapper with pip, you can run the command 

```
python -m pip install -vv --no-deps --ignore-installed .
```

Now, you should be able to go to any directory and import the Lenstool module

```python
import lenstool
```

Remember to activate the lenstool conda environment every time you open a new Terminal, and want to use Lenstool.
