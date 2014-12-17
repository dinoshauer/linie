"""Linie handlers test specs."""

import logging
from testfixtures import LogCapture
from unittest import TestCase

from linie import handlers, exceptions
from linie.handlers import DEFAULT_FORMAT, _check_keys, _check_values, _get_fmts


class TestStreamHandlerPrivates(TestCase):

    """Test private functions of the stream handler."""

    def setUp(self):
        """Set up mocks."""
        self.mock_fmts = {
            'date': '%Y-%m-%d %H:%M:%S',
            'log': '%(asctime)s [%(levelname)s] %(message)s',
        }

    def test__check_keys(self):
        """Assert that the function can compare two lists."""
        result = _check_keys(self.mock_fmts.keys(), self.mock_fmts.keys())
        assert result is True
        with self.assertRaises(exceptions.InvalidListError):
            _check_keys(['foo'], ['bar'])

    def test__check_values(self):
        """The function can check that a list of values is a specific type."""
        result = _check_values(self.mock_fmts.values(), str)
        assert result is True
        with self.assertRaises(exceptions.InvalidValueType):
            _check_values([1], str)

    def test__get_fmts(self):
        """The function should return a tuple of ``str``s."""
        result = _get_fmts(self.mock_fmts, DEFAULT_FORMAT)
        assert type(result) is tuple
        assert type(result[0]) is str
        assert type(result[1]) is str
        assert result[0] == self.mock_fmts['log']
        assert result[1] == self.mock_fmts['date']


class TestStreamHandler(TestCase):

    """Test the functionality of the stream handler itself."""

    @staticmethod
    def _generate_check(levels, msg, name):
        """Generate the list of tuples that is needed to check logged items."""
        result = []
        for level in levels:
            result.append((name, level.upper(), msg))
        return result

    def setUp(self):
        """Set up mocks."""
        self.log_name = 'test-logger'
        self.msg = 'Hello, world!'
        self.levels = ['info', 'debug', 'warning', 'error', 'critical']
        self.check_logs = self._generate_check(self.levels, self.msg,
                                               self.log_name)

    def test_stream_handler(self):
        """Assert the stream handlers functionality."""
        with LogCapture() as l:
            logger = logging.getLogger(self.log_name)
            logger.addHandler(handlers.stream())
            for level in self.levels:
                getattr(logger, level)(self.msg)
        # l.check will raise an AssertionError if its
        # internal checks goes wrong.
        l.check(*self.check_logs)
