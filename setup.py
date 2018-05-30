#!/usr/bin/env python
#
# Copyright 2017-2018 B-Open Solutions srl.
# Copyright 2017-2018 European Centre for Medium-Range Weather Forecasts (ECMWF).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os

import setuptools


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding='utf-8').read()


version = '0.0.1.dev0'


setuptools.setup(
    name='eccodes-grib',
    version=version,
    description='Python interface to the ecCodes C library to read and write GRIB files.',
    long_description=read('README.rst'),
    author='European Centre for Medium-Range Weather Forecasts (ECMWF)',
    author_email='software.support@ecmwf.int',
    license='Apache License Version 2.0',
    url='https://github.com/ecmwf/eccodes-grib',
    packages=setuptools.find_packages(),
    include_package_data=True,
    setup_requires=[
        'pytest-runner',
    ],
    install_requires=[
        'cffi',
        'future',
        'numpy',
        'typing',
    ],
    tests_require=[
        'pytest',
    ],
    test_suite='tests',
    zip_safe=True,
    keywords='eccodes grib',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
)
