#!/usr/bin/env python
import os
from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import subprocess
import numpy as np

VERSION = '0.0.1'

README = open('README.md').read()

# flags = subprocess.check_output(['pkg-config', '--cflags-only-I', 'opencv'])
# include_dirs_list = [str(flag[2:].decode('utf-8')) for flag in flags.split()]
# include_dirs_list.append('.')
# flags = subprocess.check_output(['pkg-config', '--libs-only-L', 'opencv'])
# library_dirs_list = [str(flag) for flag in flags]
# flags = subprocess.check_output(['pkg-config', '--libs', 'opencv'])
# libraries_list = []
# for flag in flags.split():
#     libraries_list.append(str(flag.decode('utf-8')))
# 
# EXTENSIONS = [
#         Extension(
#                   "rh_aligner.common.cv_wrap_module",
#                   #[str(os.path.join(b"rh_aligner".decode('utf-8'), b"common".decode('utf-8'), b"cv_wrap_module.pyx".decode('utf-8'))), str(os.path.join(b"rh_aligner".decode('utf-8'), b"common".decode('utf-8'), b"cv_wrap.cpp".decode('utf-8')))],
#                   #[os.path.abspath(str(os.path.join(b"rh_aligner", b"common", b"cv_wrap_module.pyx"))), os.path.abspath(str(os.path.join(b"rh_aligner", b"common", b"cv_wrap.cpp")))],
#                   [os.path.abspath(os.path.join("rh_aligner", "common", "cv_wrap_module.pyx")), os.path.abspath(os.path.join("rh_aligner", "common", "cv_wrap.cpp"))],
#                   #[os.path.abspath(str(os.path.join("rh_aligner", "common", "cv_wrap_module.pyx"))), os.path.abspath(str(os.path.join("rh_aligner", "common", "cv_wrap.cpp")))],
#                   language="c++",
#                   include_dirs=include_dirs_list,
#                   extra_compile_args=['-O3', '--verbose'],
#                   extra_objects=libraries_list
#                  ),
#         Extension(
#                   "rh_aligner.common.oriented_simple_blob_detector",
#                   #[str(os.path.join(b"rh_aligner", b"common", b"oriented_simple_blob_detector.pyx")), str(os.path.join(b"rh_aligner", b"common", b"OrientedSimpleBlobDetector.cpp"))],
#                   [os.path.join("rh_aligner", "common", "oriented_simple_blob_detector.pyx"), os.path.join("rh_aligner", "common", "OrientedSimpleBlobDetector.cpp")],
#                   language="c++",
#                   include_dirs=include_dirs_list,
#                   extra_compile_args=['-O3', '--verbose'],
#                   extra_objects=libraries_list
#                  ),
#         Extension(
#                   "rh_aligner.common.vfc_filter",
#                   #[str(os.path.join(b"rh_aligner", b"common", b"vfc_filter.pyx")), str(os.path.join(b"rh_aligner", b"common", b"vfc.cpp"))],
#                   [os.path.join("rh_aligner", "common", "vfc_filter.pyx"), os.path.join("rh_aligner", "common", "vfc.cpp")],
#                   language="c++",
#                   include_dirs=include_dirs_list,
#                   extra_compile_args=['-O3', '--verbose'],
#                   extra_objects=libraries_list
#                  ),
#         Extension(
#                   "rh_aligner.alignment.mesh_derivs_multibeam",
#                   #[str(os.path.join(b"rh_aligner", b"alignment", b"mesh_derivs_multibeam.pyx"))],
#                   [os.path.join("rh_aligner", "alignment", "mesh_derivs_multibeam.pyx")],
#                   include_dirs=[np.get_include()],
#                   extra_compile_args=['-fopenmp', '-O3', '--verbose'],
#                   extra_link_args=['-fopenmp']
#                  )
# ]
# 
setup(
    name='mb_aligner',
    version=VERSION,
#     packages=find_packages(exclude=['*.common']),
#     ext_modules = cythonize(EXTENSIONS),
    author='Adi Suissa-Peleg',
    author_email='adisuis@seas.harvard.edu',
    url="https://code.harvard.edu/adp560/mb_aligner",
    description="Rhoana's 2D and 3D alignment tool for a multibeam microscope images",
    long_description=README,
    include_package_data=True,
    install_requires=[
        "numpy>=1.13.0",
        "scipy>=0.16.0",
        "argparse>=1.4.0",
        "h5py>=2.5.0",
        "Cython>=0.23.3",
        "opencv_contrib_python>=3.3.0",
    ],
    dependency_links = [
        'http://github.com/Rhoana/rh_renderer/tarball/master#egg=rh_renderer-0.0.1',
        'http://github.com/Rhoana/rh_config/tarball/master#egg=rh_config-1.0.0',
        'http://github.com/Rhoana/rh_logger/tarball/master#egg=rh_logger-2.0.0'
    ],
    zip_safe=False
)