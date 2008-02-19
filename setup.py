# Copyright (c) 2007-2008 The RTMPy Project.
# See LICENSE for details.

from ez_setup import use_setuptools

use_setuptools()

import sys
from setuptools import setup, find_packages

install_requires = ['Twisted>=2.5.0', 'PyAMF>=0.1.1']

if sys.platform.startswith('win'):
    install_requires.append('PyWin32')

long_desc = """\
RTMPy is a Twisted protocol implementing Adobe's Real
Time Messaging Protocol (RTMP), used for full-duplex
real-time communication with applications running inside
the Flash Player."""

keyw = """\
rtmp flv rtmps rtmpe amf amf0 amf3 flex flash http https
streaming video audio sharedobject webcam record playback
flashplayer air actionscript decoder encoder gateway"""

setup(name = "RTMPy",
    version = "0.1",
    description = "Twisted protocol for RTMP",
    long_description = long_desc,
    url = "http://rtmpy.org",
    author = "The RTMPy Project",
    author_email = "rtmpy-dev@rtmpy.org",
    keywords = keyw,
    packages = ["rtmpy"],
    test_suite = "rtmpy.tests.suite",
    install_requires = install_requires,
    license = "MIT License",
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ])
