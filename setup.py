#!/usr/bin/env python2

import os
import re
from setuptools import setup, find_packages

def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name), 'r') as f:
        filestring = f.read()
    return filestring


def get_version():
    raw_init_file = read("kismetexternal/__init__.py")
    rx_compiled = re.compile(r"\s*__version__\s*=\s*\"(\S+)\"")
    ver = rx_compiled.search(raw_init_file).group(1)
    return ver

setup(name='kismetexternal',
      version=get_version(),
      description='Kismet External Helper Library',
      author='Mike Kershaw / Dragorn',
      author_email='dragorn@kismetwireless.net',
      url='https://www.kismetwireless.net/',
      install_requires=['protobuf >= 3.0.0'],
      packages=find_packages(),
     )


