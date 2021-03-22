CHANGES
=======

4.1.0 (unreleased)
------------------

- Add support for Python 3.7, 3.8 and 3.9.

- Drop support for Python 3.4.

- Fix tests to run with ``zope.component >= 5``.


4.0.1 (2017-05-15)
------------------

- Fix rendering of user errors on Python 3.
  See `issue 2 <https://github.com/zopefoundation/zope.app.exception/issues/2>`_.


4.0.0 (2017-05-01)
------------------

- Add support for PyPy, and Python 3.4, 3.5 and 3.6.

- Remove test dependency on ``zope.app.testing``,
  ``zope.app.zcmlfiles`` and many others.

3.6.3 (2011-05-23)
------------------

- Replaced an undeclared test dependency on ``zope.app.authentication`` with
  ``zope.password``.


3.6.2 (2010-09-14)
------------------

- No longer depend on ``zope.app.zptpage`` for tests.

- Replaced dependency on ``zope.app.securitypolicy`` by
  ``zope.securitypolicy``.


3.6.1 (2010-01-08)
------------------

- Require zope.browserpage which now contains ``namedtemplate``.

- Fix ftesting.zcml due to ``zope.securitypolicy`` update.

- Fix tests using a newer zope.publisher that requires zope.login.

3.6.0 (2009-05-18)
------------------

- ``ISystemErrorView`` interface has been moved to
  ``zope.browser.interfaces``, leaving BBB import here.

- Cut dependency on ``zope.formlib`` by requiring newer version of
  ``zope.app.pagetemplate`` which now contains ``namedtemplate``.


3.5.0 (2009-04-06)
------------------

- Use new ``zope.authentication`` instead of ``zope.app.security``.

- Removed deprecated code and thus removed dependency on zope.deferredimport.

- Removed old zpkg-related SETUP.cfg file.

3.4.2 (2009-01-27)
------------------

- Substitute zope.app.zapi by direct calls to its wrapped apis. See
  bug 219302.

- Fixed author email and home page.


3.4.1 (2007-10-31)
------------------

- Resolve ``ZopeSecurityPolicy`` deprecation warning.


3.4.0 (2007-10-24)
------------------

- Initial release independent of the main Zope tree.
