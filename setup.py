# encoding: utf-8

from setuptools import setup

setup(
    name              = 'flock',
    version           = '0.1',
    description       = 'Flock object for with statement ',
    author            = 'Jakub Dorňák',
    author_email      = 'jdornak@redhat.com',
    url               = 'https://github.com/misli/python-flock',
    py_modules        = ['flock'],
    long_description  = 'Flock uses fcntl.flock to lock (resp. unlock) '
                        'file descriptor (fd) with operation (op) '
                        'when entering (resp. leaving) runtime context related to it.'
)
