##############################################################################
#
# Copyright (c) 2006-2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.app.exception package
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


version = '4.1.0.dev0'

tests_require = [
    'webtest',

    'zope.app.appsetup',
    'zope.app.basicskin >= 4.0',
    'zope.app.pagetemplate',
    'zope.app.publication',
    'zope.app.wsgi',

    'zope.browsermenu',
    'zope.browserresource',
    'zope.container',
    'zope.login',
    'zope.password',
    'zope.principalregistry',
    'zope.publisher',
    'zope.securitypolicy',
    'zope.site',
    'zope.testrunner',
]

setup(name='zope.app.exception',
      version=version,
      author='Zope Corporation and Contributors',
      author_email='zope-dev@zope.org',
      description='Zope 3 exception views',
      long_description=(
          read('README.rst')
          + '\n\n' +
          '.. contents::'
          + '\n\n' +
          read('src', 'zope', 'app', 'exception', 'browser', 'systemerror.rst')
          + '\n\n' +
          read('CHANGES.rst')
      ),
      keywords="zope3 exception view",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope :: 3',
      ],
      url='http://pypi.python.org/pypi/zope.app.exception',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope', 'zope.app'],
      extras_require={
          'test': tests_require,
      },
      tests_require=tests_require,
      install_requires=[
          'setuptools',
          'zope.interface',
          'zope.publisher >= 3.12',
          'zope.authentication',
          'zope.browser>=1.2',
          'zope.browserpage>=3.11.0',
          'zope.component',
          'zope.security',
      ],
      include_package_data=True,
      zip_safe=False,
      )
