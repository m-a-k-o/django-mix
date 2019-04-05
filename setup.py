# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


version = '1.0.0'


setup(
    name='djangomix',
    version=version,
    keywords='Django Mix',
    description='Django integration for Laravel Mix',
    long_description=open('README.md').read(),

    url='https://github.com/m-a-k-o/django-mix',

    author='Marek Racik',
    author_email='marek@racik.info',

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
