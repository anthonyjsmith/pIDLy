#!/usr/bin/env python

from distutils.core import setup

setup(name='pIDLy',
      version='0.2.4',
      description='IDL within Python',
      long_description='Control ITT\'s IDL (Interactive Data Language) from within Python',
      author='Anthony Smith',
      author_email='A.J.Smith@sussex.ac.uk',
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
