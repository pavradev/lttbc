#!/usr/bin/env python
import os.path as osp
import sys

from setuptools import Extension, setup


def get_script_path():
    return osp.dirname(osp.realpath(sys.argv[0]))


# def read(*parts):
#     return open(osp.join(get_script_path(), *parts)).read()


class numpy_get_include:
    def __str__(self):
        import numpy
        return numpy.get_include()


lttbc_py = Extension("lttbc", sources=["lttbc.c"],
                     define_macros=[
                         ("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
                     include_dirs=[numpy_get_include(),
                                   get_script_path()],
                     )

setup(
    name="plttbc",
    author="Pavel Rabetski",
    version="0.2.4",
    #use_scm_version=True,
    ext_modules=[lttbc_py],
    author_email="rabeckijps@gmail.com",
    maintainer="Pavel Rabetski",
    url="https://github.com/pavradev/lttbc/",
    description="Largest triangle three buckets module for Python written in C",
    #long_description=read("README.txt"),
    long_description_content_type="text/markdown",
    license="MIT",
    install_requires=["numpy"],
    setup_requires=["setuptools_scm"],
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)
