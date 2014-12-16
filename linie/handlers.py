"""Linie log handlers."""

import logging
import sys

from . import exceptions

__all__ = ('stream', )
DEFAULT_FORMAT = {
    'date': '%Y-%m-%d %H:%M:%S',
    'log': '%(asctime)s [%(levelname)s] %(message)s',
}


def _check_keys(keys, spec):
    """Check a list of ``keys`` equals ``spec``.

    Sorts both keys and spec before checking equality.

    Arguments:
        keys (``list``): The list of keys to compare to ``spec``
        spec (``list``): The list of keys to compare to ``keys``

    Returns:
        ``bool``

    Raises:
        ``exceptions.InvalidListError``: Raised if ``keys`` is not
            equal to ``spec``.
    """
    if not sorted(keys) == sorted(spec):
        raise exceptions.InvalidListError('{} does not equal {}'.format(key, spec))
    return True


def _check_values(values, spec):
    """Check that a list of ``values`` are of the ``spec`` type.

    Arguments:
        values (``list``): List of values to check
        spec (``type``): The type to check for

    Returns:
        ``bool``

    Raises:
        ``exceptions.InvalidValueType``: Raised it the values are not
            of type ``spec``.
    """
    for value in values:
        if type(value) is not spec:
            error = '{} is not of type {}'.format(value, spec)
            raise exceptions.InvalidValueType(error)
    return True


def _get_fmts(fmt, spec):
    """Get formats to use with ``logging.Formatter``.

    Arguments:
        fmt (``dict``): The input dict to check
        spec (``dict``): The spec dict to check against ``fmt``

    Returns:
        ``tuple`` (log_fmt, date_fmt)
    """
    if _check_keys(fmt.keys(), spec.keys()):
        if _check_values(fmt.values(), str):
            return fmt['log'], fmt['date']


def stream(stream=sys.stdout, fmt=DEFAULT_FORMAT):
    """Log handler that will write to a ``file``-like object like ``stdout``.

    Arguments:
        stream (``file`` optional): Any object which supports write() & flush()
            methods (From the ``logging.StreamHandler`` see link in Notes)
            Default: ``sys.stdout``
        fmt (``dict``, optional): Set the format for the handler.
            Default: {
                'date': '%Y-%m-%d %H:%M:%S',
                'log': '%(asctime)s [%(levelname)s] %(message)s',
            }

    Notes:
        docs.python.org/2/library/logging.handlers.html#logging.StreamHandler
    """
    log_fmt, date_fmt = _get_fmts(fmt, DEFAULT_FORMAT)
    handler = logging.StreamHandler(stream)
    handler.setFormatter(logging.Formatter(log_fmt, date_fmt))
    return handler
