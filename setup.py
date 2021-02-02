#!/usr/bin/env python

from setuptools import setup, find_packages

install_requires = [
    'websocket-client>=0.40.0',
    'protobuf'
]

tests_require = [
    'pytest',
    'python-dateutil>=2.7.5',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='openfeed',
    version='1.1.5',
    author='Barchart',
    author_email='mike@barchart.com',
    license='MIT',
    url='https://github.com/openfeed-org/sdk-python',
    include_package_data=True,
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require
    },
    description='Barchart Openfeed Example Client for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    download_url='https://github.com/openfeed-org/sdk-python/archive/master.zip',
    keywords=[]
)
