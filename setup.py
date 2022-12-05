"""Package setup"""
from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='stringdb_alias',
    version='1.0',
    author='Yuriy Sverchkov',
    author_email='yuriy.sverchkov@wisc.edu',
    description=
        'A python package for working with string-db.org aliases (gene and protein ID mapping).',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='https://github.com/Craven-Biostat-Lab/stringdb_alias',
    license='MIT',
    packages=['stringdb_alias'],
    install_requires=['pandas'],
    classifiers=["Programming Language :: Python :: 3"],
    python_requires='>=3.6'
)
