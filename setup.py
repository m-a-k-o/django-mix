# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


version = '1.1.2'


# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='djangomix',
    version=version,
    keywords='Django Mix',
    description='Django integration for Laravel Mix',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/m-a-k-o/django-mix',

    author='Marek Racik',
    author_email='marek@idea-loop.com',

    packages=find_packages(),
    requires=[
        'Django (>=1.11)',
    ],
    install_requires=[
        'Django>=1.11',
    ],

    include_package_data=True,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
