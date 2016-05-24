#!/usr/bin/env python3

import sys

# Try using setuptools first, if it's installed
from setuptools import setup, find_packages

# Need to add all dependencies to setup as we go!
setup(name='PyCmdMessenger',
      packages=['PyCmdMessenger'],
      version='0.1',
      description='Python interface for CmdMessenger arduino serial communication library',
      author='Michael J. Harms',
      author_email='harmsm@gmail.com',
      url='https://github.com/harmsm/PyCmdMessenger',
      download_url='https://XX',
      zip_safe=False,
      install_requires=["pyserial"],
      classifiers=['arduino','raspberry pi','serial','usb'])

