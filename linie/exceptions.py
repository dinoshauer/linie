"""Exceptions used in the linie module."""


class LinieError(Exception):

    """Linie base exception."""


class InvalidDictError(LinieError):

    """Exception to be raised when a dict is invalid according to spec."""


class InvalidValueType(LinieError):

    """Exception to be raised when a value is of a wrong type."""


class InvalidListError(LinieError):

    """Exception to be raised when a list does not equal another list."""
