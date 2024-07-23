# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

try:
    path_lenstool = '/home/joseph/Software/Lenstool_JA' # os.getenv(LENSTOOL_DIR)
    sys.path.insert(0, os.path.abspath(path_lenstool)) # '/path_to_lenstool/' '/home/joseph/Software/lenstool/'
    #import lenstool
    #print("Path of lenstool:", lenstool.__file__)
    #print("lenstool.constant.cH0_4piG = ", lenstool.constant.cH0_4piG)
    #sys.path.insert(0, os.path.abspath("/home/joseph/Software/Lenstool_JA/lenstool"))
    print("Lenstool directory imported: " + path_lenstool)
except:
    print("WARNING: No 'LENSTOOL_DIR' variable found, the path to Lenstool is unknown.")

# -- Project information -----------------------------------------------------

project = 'Lenstool'
copyright = '2024, Lenstool group'  
author = 'Lenstool group' # Jean-Paul Kneib, Henri Bonnet, Ghyslain Golse, David Sand, Eric Jullo, Phil Marshall, Julien Zoubian, Mathilde Jauzac, Johan Richard, Benjamin Clément, Tomas Verdugo, Soniya Sharma, Benjamin Beauchesne, Joseph Allingham (Do we miss someone?)

three_dir_up = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../../../")
version_file = three_dir_up + "/VERSION"
with open(version_file, 'r') as file:
    version = file.read()
print("VERSION: " + version)

# Last version number for which it was compiled, not necessarily the last 
# release = '8.5'   
# version = '8.5.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.imgmath', 
    'sphinx.ext.todo',
    'myst_nb',

#    'breathe',   # add it if doing C api. Requires to install breathe.
#    'sphinx.ext.duration',
#    'sphinx.ext.autosummary',
#    'sphinx.ext.intersphinx',
]
#nb_kernel_rgx_aliases = {"python3"}
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

myst_enable_extensions = ["dollarmath", "amsmath"]

# Execute notebooks during Sphinx build process
nbsphinx_execute = 'auto'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

nb_kernel_rgx_aliases = {"lt_test": "python"}
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme' # 'haiku' # 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here, relative to this directory. They are copied after the builtin static files, so a file named "default.css" will overwrite the builtin "default.css".

#html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Extension configuration -------------------------------------------------
if False:
    import subprocess
    subprocess.call('make clean', shell=True)
    subprocess.call('cd ../../doxygen ; doxygen', shell=True)

    breathe_projects = { "lenstool": "../../../docs/doxygen/build/xml/" }
    breathe_default_project = "lenstool"
    breathe_projects_source = {
        "o_chi" : ( "../../../../src", ["o_chi.c"] )
    }


# If necessary, eliminate some Myst Warnings:
# import warnings
# warnings.filterwarnings("ignore", category=UserWarning, message=".*'myst' cross-reference target not found.*")
