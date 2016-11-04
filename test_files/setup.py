from distutils.core import setup

from setuptools.command.test import test as TestCommand

setup(
    #...,
    tests_require=['pytest'],
    )