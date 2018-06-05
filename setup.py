# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='catalogue',
    version='0.1.0',
    description='Resource management with Alfred',
    long_description=readme,
    author='Wessel Bruinsma',
    author_email='skeleton_author_email',
    url='https://github.com/wesselb/catalogue',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)