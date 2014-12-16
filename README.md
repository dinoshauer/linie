Linie
=====

A collection of handy utilities for logging.

## KwargLogger

    from linie import loggers, handlers


    log = loggers.KwargLogger()
    log.addHandler(handlers.stream())

    log.info('Hello World', process_num=1)
    log.info('Some object', dump={'foo': 'bar'})
