# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.0'


setup(
    name='djago-mix',
    version=version,
    keywords='Django Mix',
    description='Pythonoic mix(originated by Laravel) function for working with laravel-mix inside django apps',
    long_description=open('README.md').read(),

    url='https://github.com/m-a-k-o/django-mix',

    author='Marek Racik',
    author_email='marek@racik.info',

    packages=['django-mix'],
    py_modules=[],
    install_requires=[],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
