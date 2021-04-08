#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

# with open('HISTORY.rst') as history_file:
#    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Tomas Johansson",
    author_email='pypi@programmerare.com',
    python_requires='>=2.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Topic :: Scientific/Engineering :: GIS",        
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Python constants with EPSG numbers for coordinate reference systems, based on EPSG dataset v10.011",
    install_requires=requirements,
    license="MIT license",
    # long_description=readme + '\n\n' + history,
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='EPSG constants,CRS,Coordinate Reference Systems',
    name='epsg-constants',
    packages=find_packages(include=['epsg_constants', 'epsg_constants.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/TomasJohansson/epsg_constants_4python',
    version='10.11.0',
    zip_safe=False,
)
