#!/usr/bin/env python

import argparse
from path import path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bootstrap app for Sublime projects.')
    parser.add_argument('name',
                        action='store',
                        default=path(__file__).dirname(),
                        help='Name of the sublime config file (default is directoryname.sublime-project).')
    parser.add_argument('--import-gitignore',
                        dest='gitignore',
                        action='store_true',
                        default=None,
                        help='Add ignored patterns from your gitignore file (trailing "/" in pattern assumed to be folder).')
    parser.add_argument('--import-system-gitignore',
                        dest='sysgitignore',
                        action='store_true',
                        default=None,
                        help='Add ignored patterns from your system gitignore file (trailing "/" in pattern assumed to be folder).')
    parser.add_argument('-s', '--import-slickedit',
                        action='store',
                        dest='slickedit',
                        help='Parse a SlickEdit project file.')

    args = parser.parse_args()
