#!/usr/bin/env python

from setuptools import setup

version = "0.0.23"

setup(
    name="pycoinrpc",
    version=version,
    packages = [
      "txfilter",
    ],
    author="Jonn Mostovoy",
    entry_points = { 'console_scripts':
            [
                'txfilterd = txfilter.daemon:main',
            ]
        },
    author_email="amarr.industrial@gmail.com",
    url="https://github.com/manpages/stupid-transaction-filter",
    license="http://opensource.org/licenses/MIT",
    description="Poorly documented and quite inefficient Bitcoin transaction filter."
)
