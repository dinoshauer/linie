"""Linie loggers test specs."""

import logging
from testfixtures import LogCapture
from unittest import TestCase

from linie import loggers, handlers


class TestKwargLogger(TestCase):

    """Test the functionality of the KwargLogger logger9."""

    @staticmethod
    def _generate_check(levels, msg, name, kwargs):
        """Generate the list of tuples that is needed to check logged items."""
        result = []
        for level in levels:
            result.append((name, level.upper(), msg))
        return result

    def setUp(self):
        """Set up mocks."""
        logging.setLoggerClass(loggers.KwargLogger)

        self.log_name = 'test-logger'
        self.msg = 'Hello, world!'
        self.log_kwargs = {'foo': 'bar', }
        self.levels = ['info', 'debug', 'warning', 'error', 'critical']
        self.logger = logging.getLogger(self.log_name)
        self.logger.addHandler(handlers.stream())
        self.check_logs = self._generate_check(
            self.levels,
            self.logger._build_msg(self.msg, self.log_kwargs),
            self.log_name,
            self.log_kwargs,
        )

    def test__parse_kwargs(self):
        """Assert that the _parse_kwargs method can filter a dict."""
        kwargs = {'exc_info': '', 'extra': '', 'foo': 'bar', 'bar': 'baz'}
        result = loggers.KwargLogger._parse_kwargs(kwargs)
        assert {'exc_info', 'extra', } not in result.keys()
        assert ['foo', 'bar', ] == result.keys()

    def test_logger_output(self):
        """Assert that the logger will output with the default format."""
        with LogCapture() as l:
            for level in self.levels:
                getattr(self.logger, level)(self.msg, **self.log_kwargs)
        # l.check will raise an AssertionError if its
        # internal checks goes wrong.
        l.check(*self.check_logs)

    def test_build_msg(self):
        """Assert that the logger will build the message correctly."""
        result = self.logger._build_msg(self.msg, self.log_kwargs)
        assert result == 'Hello, world! - foo=bar'

    def test_build_msg_with_custom_formatter(self):
        """Assert that _build_msg can use a custom formatter."""
        def foo_formatter(msg, kwargs, fmt):
            """Format a log message."""
            return 'foo'

        self.logger.formatter = foo_formatter
        with LogCapture() as l:
            self.logger.info(self.msg)
        l.check((self.log_name, 'INFO', 'foo'))
        self.logger.formatter = None

    def test_logging_with_custom_fmt(self):
        """Assert that a custom ``fmt`` can be used."""
        fmt = self.logger.fmt
        self.logger.fmt = '{}: {}'
        with LogCapture() as l:
            self.logger.info(self.msg, **self.log_kwargs)
        l.check(
            (self.log_name, 'INFO', '{} - {}: {}'.format(
                self.msg, 'foo', 'bar'
            ))
        )
        self.logger.fmt = fmt
