from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy
import os
import imp

VERSION = imp.load_source('version', os.path.join('.', 'version.py'))
VERSION = VERSION.__version__

setup(
    version=VERSION,
	name='sort',
    description='SORT',
    license='GPLv3',
    packages = find_packages(),
    install_requires=['numba', 'numpy', 'scikit-image', 'matplotlib', 'sklearn', 'FilterPy']
)