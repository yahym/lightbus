#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

setup(
    name='lightbus',
    version=open('VERSION').read().strip(),
    author='Adam Charnock',
    author_email='adam@adamcharnock.com',
    packages=find_packages(),
    scripts=[],
    url='http://lightbus.org',
    license='MIT',
    description='Filling the gap between monolithic and microservice',
    long_description=open('README.rst').read() if exists("README.rst") else "",
    install_requires=[
        'asyncio_extras>=1.3.0,<1.4.0',
        'aioredis',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'lightbus = lightbus.commands:lightbus_entry_point',
        ]
    }
)
