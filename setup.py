# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup

setup(name="ssllabs_scan",
    version="0.1",
    description="API for SSLLabs scanning service",
    packages=['scan'],
    test_suite="tests",
)
