from setuptools import setup, Extension

INCLUDE_DIRS = ['../common']

try:
    import numpy as np
    INCLUDE_DIRS.insert(0, np.get_include())
except ImportError:
    pass

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'pycocotools._mask',
        sources=['../common/maskApi.c', 'pycocotools/_mask.pyx'],
        include_dirs = INCLUDE_DIRS,
        extra_compile_args=['-std=c99'],
    )
]

setup(
    name='pycocotools',
    packages=['pycocotools'],
    package_dir = {'pycocotools': 'pycocotools'},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0',
        'numpy>=1.18.1',
    ],
    version='2.0',
    ext_modules= ext_modules
)
