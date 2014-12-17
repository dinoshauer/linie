Stream Handler example
======================

The stream handler writes to any file-like stream/object. It defaults to 
``sys.stdout``. Using the stream handler is straight-forward.
It can be used with any logger.

Here's an example using the standard ``logging`` module::

    import logging

    from linie import handlers

    log = logging.getLogger()
    log.setLevel(logging.INFO)

    log.addHandler(handlers.stream())

    log.info('Hello World')


and here it is used with a linie logger::

    from linie import loggers, handlers


    log = loggers.KwargLogger()
    log.addHandler(handlers.stream())

    log.info('Hello World')
