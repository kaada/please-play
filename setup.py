#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md") as readme_file:
    readme_data = readme_file.read()

setup(
    name="please-play",
    description="Play YouTube music from your terminal with ease.",
    long_description=readme_data,
    author="Olav Kaada",
    author_email="mail@okaada.com",
    url="https://github.com/kaada/please-play",
    classifiers=[
        "Topic :: Software Development",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "mpv"
    ],
    packages=["please-play"],
)
