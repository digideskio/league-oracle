#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='oracle',
      version='0.0.1',
      description='GroupMe League Oracle',
      author='Doug Black',
      author_email='doug@dougblack.io',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'requests',
          'flask'
      ])
