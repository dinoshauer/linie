"""Setup file for handling the linie package."""

from setuptools import setup

import linie

setup(
    name=linie.__name__,
    description=linie.__doc__,
    license='MIT',
    url=linie.__url__,
    author=linie.__author__,
    author_email=linie.__email__,
    packages=[
        'linie',
    ],
    version=linie.__version__,
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
)
