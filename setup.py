#-*- coding:utf-8 -*-


import setuptools
from sphinxcontrib import twitter as pkg

pkgname = pkg.__name__

setuptools.setup(
    name=pkgname,
    version=pkg.__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'sphinx'
        ],
    author=pkg.__author__,
    license=pkg.__license__,
    url='https://github.com/coding-to-music/sphinx-seometatwitter',
    description='SEO meta in header and embed twitter tweet in sphinx.',
    long_description=pkg.__doc__,
    namespace_packages=['sphinxcontrib'],
    classifiers='''
Programming Language :: Python
License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Topic :: Software Development :: Documentation
'''.strip().splitlines())

