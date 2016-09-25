#! /usr/bin/env python3.5
"""
this is just a simple setup script for my parse library that sits on top of the optparse module
"""
from distutils.core import setup

setup(
    name="parse",
    version="1.0.0",
    packages=["parse"],
    author="Danny mcwaves",
    author_email="dannymcwaves96@gmail.com",
    url="https://github.com/DannyMcwaves",
    description="A simple commandline specification tool/parser built on top of the optparse module",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
