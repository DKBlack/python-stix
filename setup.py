# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from setuptools import setup, find_packages

setup(
    name="stix",
    version="1.0.0a2",
    author="STIX Project, MITRE Corporation",
    author_email="stix@mitre.org",
    description="An API for parsing and generating STIX content.",
    url="http://stix.mitre.org",
    packages=find_packages(),
    install_requires=['lxml>=2.3', 'python-dateutil', 'cybox>=2.0.0a1' ],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)
