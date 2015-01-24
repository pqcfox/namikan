#!/usr/bin/env/python
from setuptools import setup

setup(
    name = 'namikan',
    version = '1.0',
    description = 'An epic curses game written in Python for the enjoyment of all.',
    packages = ['namikan'],
    include_package_data = True,
    entry_points = {
        'console_scripts': [
            'namikan = namikan.namikan:run'
        ]
    }
)
      


