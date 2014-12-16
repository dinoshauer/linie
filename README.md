Linie
=====

http://linie.readthedocs.org/en/latest/

A collection of handy utilities for logging.

## KwargLogger

    >>> from linie import loggers, handlers
    >>>
    >>>
    >>> log = loggers.KwargLogger()
    >>> log.addHandler(handlers.stream())
    >>>
    >>> log.info('Hello World', process_num=1)
    2014-12-16 08:08:34 [INFO] Hello World - process_num=1
    >> log.info('Some object', dump={'foo': 'bar'})
    2014-12-16 08:08:34 [INFO] Some object - dump={'foo': 'bar'}
