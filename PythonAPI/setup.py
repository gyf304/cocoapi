from setuptools import dist, setup, Extension

dist.Distribution().fetch_build_eggs(['Cython>=0.27.3', 'numpy>=1.18.1'])

import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'pycocotools._mask',
        sources=['../common/maskApi.c', 'pycocotools/_mask.pyx'],
        include_dirs=[np.get_include(), '../common'],
        extra_compile_args=['-std=c99'],
    )
]

setup(
    name='pycocotools',
    packages=['pycocotools'],
    package_dir = {'pycocotools': 'pycocotools'},
    install_requires=[
        'setuptools>=18.0',
        'Cython>=0.27.3',
        'matplotlib>=2.1.0',
        'numpy>=1.18.1',
    ],
    version='2.0',
    ext_modules= ext_modules
)
