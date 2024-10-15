"""
File: setup.py
Author: Steven "Kabbe" Karbjinsky
Description: Setup configuration for the AstroLens backend project.

For more information, see: https://github.com/xKabbe/astrolens
"""
from setuptools import setup, find_packages

setup(
    name='astrolens',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.12',
    author='Steven Karbjinsky',
    author_email='steven.karbjinsky@web.de',
    url='https://github.com/xKabbe/astrolens'
)