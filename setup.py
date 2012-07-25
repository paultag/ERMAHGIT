#!/usr/bin/env python
# Copyright (c) Paul Tagliamonte <paultag@debian.org> under the terms and
# conditions of the Expat license.

from setuptools import setup

setup(
    name       = "ERMAHGIT",
    version    = "0.0.never.use.this.0",

    packages   = [
        'ermahgerd'
    ],

    author       = "Paul Tagliamonte",
    author_email = "paultag@debian.org",
    description      = 'foobar',
    license          = "Expat",
    url              = "http://pault.ag",
    platforms        = ['any'],
    scripts=['ermahgit', 'ermahgit-translate']
)
