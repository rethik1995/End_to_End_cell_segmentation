# This will treat any local package as a python package
from setuptools import find_packages,setup

setup(
    name = 'cellsegmentation',
    version = '0.0.0',
    author='Rethik Bhat',
    author_email='rethik.bhat@gmail.com',
    packages=find_packages(),
    install_requires = []
)