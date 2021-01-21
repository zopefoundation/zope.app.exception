System Errors
=============

System Errors are errors representing a system failure.  At the
application level, they are errors that are uncaught by the
application and that a developer hasn't provided a custom error view
for.

Zope provides a default system error view that prints an obnoxius
terse message and that sets the response status.

There is a simple view registered in ``ftesting.zcml`` which raises
``Exception()``:

  >>> print(http(r"""
  ... GET /error.html HTTP/1.1
  ... """))
  HTTP/1.1 500 Internal Server Error
  ...
    A system error occurred.
  ...

Another way of getting a system error is the occurrence of a system
error, such as ``ComponentLookupError``. I have registered a simple
view in ``ftesting.zcml``, too, that will raise a component lookup
error. So if we call ``componentlookuperror.html``, we should get the
error message:

  >>> print(http(r"""
  ... GET /componentlookuperror.html HTTP/1.1
  ... """))
  HTTP/1.1 500 Internal Server Error
  ...
    A system error occurred.
  ...
