#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='cloudflare',
    version='0.0.1',
    description="STILL UNDER DEVELOPMENT! Provides a CLI and Python wrappers for CloudFlare's REST API",
    long_description=readme + '\n\n' + history,
    author="Daryl Yu",
    author_email='dyu@fastmail.com',
    url='https://github.com/darylyu/cloudflare-python',
    packages=[
        'cloudflare',
    ],
    package_dir={'cloudflare':
                 'cloudflare'},
    entry_points={'console_scripts': ['cloudflare = cloudflare.cli.main']},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='cloudflare',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
