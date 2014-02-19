#!/usr/bin/env python

from setuptools import setup

setup(name='pIDLy',
      version='0.2.5',
      description='IDL within Python',
      long_description='Control ITT\'s IDL (Interactive Data Language) from within Python',
      author='Anthony Smith',
      author_email='anthonysmith80@gmail.com',
      url='https://github.com/anthonyjsmith/pIDLy',
      py_modules=['pidly'],
      license='MIT',
      requires=['NumPy', 'Pexpect'],
      install_requires=['numpy', 'pexpect'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Science/Research',
                   'Programming Language :: Other',
                   'License :: OSI Approved :: MIT License']
      )
