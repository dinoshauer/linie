"""Linie log handlers."""

import logging
import json
import sys

"""
``'threadName'``,
``'name'``,
``'thread'``,
``'created'``,
``'process'``,
``'processName'``,
``'args'``,
``'module'``,
``'filename'``,
``'levelno'``,
``'exc_text'``,
``'pathname'``,
``'lineno'``,
``'msg'``,
``'exc_info'``,
``'funcName'``,
``'relativeCreated'``,
``'levelname'``,
``'msecs'``
"""


class JsonFormatter(logging.Formatter):
    def format(self, record):
        """Format a record into a ``dict`` and JSON serialize it.

        A modified version of ``logging.Formatter#format``, most of the logic
        is taken from the originating method.
        """
        message = record.getMessage()
        if record.args:
            message = message % record.args
        blob = {
            'message': message,
            'level': record.levelname,
            'logger': record.name,
        }
        if self.usesTime():
            blob['timestamp'] = self.formatTime(record, self.datefmt)
        if record.exc_info:
            # Cache the traceback text to avoid converting it multiple times
            # (it's constant anyway)
            if not record.exc_text:
                blob['traceback'] = self.formatException(record.exc_info).decode(sys.getfilesystemencoding(), 'replace')
                record.exc_text = self.formatException(record.exc_info)
        return json.dumps(blob)
