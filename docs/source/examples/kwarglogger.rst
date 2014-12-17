KwargLogger example
===================

We'll start out with some comparisons.

Let's log a line with ``linie.KwargLogger``::

    from linie import loggers, handlers


    log = loggers.KwargLogger()
    log.addHandler(handlers.stream())

    log.info('Hello World', process_num=1)

Results in a line like this::

    2014-12-16 21:38:32 [INFO] Hello World - process_num=1

Here's the equivalent using only the standard ``logging`` module::
    
    import sys
    import logging

    log = logging.getLogger()
    log.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s - process_num=%(process_num)s', '%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    log.addHandler(handler)

    log.info('Hello World', extra={'process_num': 1})

Results in an identical line::

    2014-12-16 21:51:55 [INFO] Hello World - process_num=1

The downside of using the standard logging library is that since,
``%(process_num)s`` is defined in the formatter a ``KeyError`` will be thrown
if it isn't passed in the ``extra`` dict. Linie's ``KwargLogger`` doesn't care
about that.
