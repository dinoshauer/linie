"""Linie log classes."""

import json
import logging

__all__ = ('KwargLogger', )


class KwargLogger(logging.getLoggerClass()):
    """A logger with extra keyword arguments.

    Send any keyword argument when you call the normal log functions
    like info, warn, debug etc.
    Inheriting from ``logging.getLoggerClass()`` ``KwargLogger`` only modifies
    the log message and makes sure that no extra keywords are sent to the
    internal ``_log`` method.

    Arguments:
        name (``str``, optional): The name of the logger to get
            *default:* ``root``
        formatter (``function``, optional): The formatter to use for
            serializing the extra ``kwargs``. Default is
            ``KwargLogger#_build_msg`` see the example output above.
            ``formatter`` must take the following arguments:
            (``str``, ``dict``, ``str``)
            The first argument is the log message, the second is the
            ``dict`` of extra arguments to build the message with, the
            third argument is ``fmt`` passed into this constructor.
            *default:* None
        fmt (``str``, optional): The format to use with the ``formatter``
            *default:* ``'{}={}'``

    **Example**::

        log.info('Hello, World!', app='my_app')

    **Example output**::

        [2014-11-21 18:14:42,192][INFO] Hello, World! - app=my_app
    """

    def __init__(self, name='root', formatter=None, fmt='{}={}', **kwargs):
        """Call super on the parent logger and set the ``formatter`` arg."""
        self.name = name
        self.formatter = formatter
        self.fmt = fmt
        super(KwargLogger, self).__init__(name, **kwargs)

    @staticmethod
    def _parse_kwargs(kwargs):
        """Parse kwargs and filter out any native keywords.

        Arguments:
            kwargs (``dict``): The keyword arguments to parse
        """
        _log_kwargs = {'exc_info', 'extra'}
        return {k:v for k, v in kwargs.items() if k not in _log_kwargs}

    def _build_msg(self, msg, kwargs):
        """Build the log message from ``msg`` and ``kwargs``.

        Arguments:
            msg (``str``): The log message to extend
            kwargs (``dict``): The dict to build into the ``msg``
        """
        if not self.formatter:
            line = ', '.join(
                [self.fmt.format(k, v) for k, v in kwargs.items()]
            )
            if line:
                return '{} - {}'.format(msg, line)
            else:
                return msg
        else:
            return self.formatter(msg, kwargs, fmt=self.fmt)

    def _log(self, level, msg, args, exc_info=None, extra=None, **kwargs):
        """Method overriding ``super._log`` only modifying the msg."""
        kwargs = self._parse_kwargs(kwargs)
        msg = self._build_msg(msg, kwargs)
        kwargs = {
            'exc_info': kwargs.get('exc_info'),
            'extra': kwargs.get('extra'),
        }
        super(KwargLogger, self)._log(level, msg, args, **kwargs)
