# coding=utf-8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypi_package_example_wjw19854",
    version="0.0.1",
    author="wjw19854",
    author_email="wjw19854@163.com",
    description="package example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wjw19854/pypi_package_example",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
