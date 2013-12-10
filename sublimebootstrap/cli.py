#!/usr/bin/env python

import argparse
import sys

from path import path

import utils
from sublimeproject import SublimeProject
from __version__ import version


def main():
    parser = argparse.ArgumentParser(description='Bootstrap app for Sublime projects.')
    parser.add_argument('files',
                        nargs='*',
                        help='Files to open in Sublime Text. If no files are given, the command will open the \
                              the *.sublime-project of the current repo, if one exists.')
    parser.add_argument('-f',
                        dest='project_file',
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
    parser.add_argument('--open',
                        dest='open',
                        action='store_true',
                        default=None,
                        help='Open the *.sublime-project file. (automatic if no arguments are given)')
    # parser.add_argument('--import-slickedit',
    #                     action='store',
    #                     dest='slickedit',
    #                     help='Parse a SlickEdit project file.')
    parser.add_argument('--version', action='version', version=version)

    args = parser.parse_args()

    # Get the root of the Git repo
    git_root = path(utils.get_git_root('.'))
    if not git_root:
        sys.exit(-1)

    # Determine where project file is located
    if args.project_file:
        sp_path = path(args.project_file)
    else:
        # Find the path to existing project file, or use default if one does not exist
        sp_path = path(utils.find_sublime_project(git_root))

    sp = SublimeProject(sp_path)

    if args.add_dirs:
        sp.add_folders(*args.add_dirs)
    if args.ignored_files:
        sp.ignore_files(*args.ignored_files)
    if args.ignored_folders:
        sp.ignore_folders(*args.ignored_folders)

    sp.save()

    if args.open:
        utils.subl(sp_path)

    if args.files:
        utils.subl(*args.files)
    else:
        if sp_path.exists():
            utils.subl(sp_path)


if __name__ == '__main__':
    sys.exit(main())
