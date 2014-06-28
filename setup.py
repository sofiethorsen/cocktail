from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import codecs
import os
import sys
import re

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long', 'tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='cocktail',
    version=find_version('cocktail', '__init__.py'),
    url='http://github.com/sofiethorsen/cocktail/',
    author='Sofie Thorsen',
    tests_require=['pytest'],
    install_requires=[],
    cmdclass={'test': PyTest},
    author_email='sofie.l.thorsen@gmail.com',
    description='Drink suggestions based on what you have at home',
    packages=['cocktail'],
    include_package_data=True,
    test_suite='cocktail.test.test_cocktail',
    zip_safe=False,
    classifiers = [
        'Programming Language :: Python',
        ],
    extras_require={
        'testing': ['pytest'],
      }
)
