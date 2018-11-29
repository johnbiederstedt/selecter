#!/usr/bin/env python

import os
from setuptools import setup

def fread(fname):
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath, 'r') as fp:
        return fp.read()

setup(
    name='selecter',
    version='0.1',
    description='simplify selecting from a list by enumerating it',
    long_description=fread('README.md'),
    keywords='list selection',
    url='https://github.com/johnbiederstedt/selecter',
    author='johnbiederstedt',
    author_email='john@johnsmail.net',
    license='MIT',
    packages=['selecter'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)
