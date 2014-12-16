[![Build Status](https://travis-ci.org/Dinoshauer/linie.svg)](https://travis-ci.org/Dinoshauer/linie)
[![Coverage Status](https://coveralls.io/repos/Dinoshauer/linie/badge.png)](https://coveralls.io/r/Dinoshauer/linie)
[![Documentation Status](https://readthedocs.org/projects/linie/badge/?version=latest)](https://readthedocs.org/projects/linie/?badge=latest)

Linie
=====

http://linie.readthedocs.org/en/latest/

For the latest development version run

    pip install linie --pre

For the latest version run

    pip install linie

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
