#!/usr/bin/env python

import argparse
import sys
import os

from path import path

import utils
from sublimeproject import SublimeProject


def find_sublime_project(git_root):
    for f in git_root.files():
        if f.isfile():
            if f.fnmatch('*.sublime-project'):
                return f
    return git_root / git_root.name + '.sublime-project'


def main():
    parser = argparse.ArgumentParser(description='Bootstrap app for Sublime projects.')
    parser.add_argument('name',
                        action='store',
                        nargs='?',
                        default=None,
                        help='Name of the sublime config file (default is <repo_root_dir_name>.sublime-project \
                              if a *.sublime-project file cannot be found in the repo root).')
    parser.add_argument('-if',
                        dest='ignored_files',
                        action='append',
                        help='Add files to the "ignore_files" section of the *.sublime-project file.')
    parser.add_argument('-id',
                        dest='ignored_folders',
                        action='append',
                        help='Add directories to the "ignore_folders" section of the *.sublime-project file.')
    parser.add_argument('-ad',
                        dest='add_dirs',
                        action='append',
                        help='Add directories to the "folders" section of the *.sublime-project file.')
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
    parser.add_argument('--install-subl',
                        dest='subl',
                        action='store_true',
                        default=None,
                        help='Install the "subl" command line tool.')
    # parser.add_argument('--import-slickedit',
    #                     action='store',
    #                     dest='slickedit',
    #                     help='Parse a SlickEdit project file.')

    args = parser.parse_args()

    # Get the root of the Git repo
    git_root = path(utils.get_git_root('.'))
    if not git_root:
        sys.exit(-1)

    # Determine where project file is located
    if args.name:
        sp_path = args.name
    else:
        # Find the path to existing project file, or use default if one does not exist
        sp_path = find_sublime_project(git_root)

    sp = SublimeProject(sp_path)

    if args.add_dirs:
        sp.add_folders(*args.add_dirs)
    if args.ignored_files:
        sp.ignore_files(*args.ignored_files)
    if args.ignored_folders:
        sp.ignore_folders(*args.ignored_folders)

    sp.save()


if __name__ == '__main__':
    sys.exit(main())
