# Sublime Bootstrap
===================

A small program to easily set up a Sublime Text project file.

## Installation

## Usage

View the help for this tool by executing the following command in a shell:

    $ subl -h
    usage: subl [-h] [-f [PROJECT_FILE]] [-if IGNORED_FILES] [-id IGNORED_FOLDERS]
                [-ad ADD_DIRS] [--import-gitignore] [--import-system-gitignore]
                [--open] [--version]
                [files [files ...]]

    Bootstrap app for Sublime projects.

    positional arguments:
      files                 Files to open in Sublime Text. If no files are given,
                            the command will open the the *.sublime-project of the
                            current repo, if one exists.

    optional arguments:
      -h, --help            show this help message and exit
      -f [PROJECT_FILE]     Name of the sublime config file (default is
                            <repo_root_dir_name>.sublime-project if a *.sublime-
                            project file cannot be found in the repo root).
      -if IGNORED_FILES     Add files to the "ignore_files" section of the
                            *.sublime-project file.
      -id IGNORED_FOLDERS   Add directories to the "ignore_folders" section of the
                            *.sublime-project file.
      -ad ADD_DIRS          Add directories to the "folders" section of the
                            *.sublime-project file.
      --import-gitignore    Add ignored patterns from your gitignore file
                            (trailing "/" in pattern assumed to be folder).
      --import-system-gitignore
                            Add ignored patterns from your system gitignore file
                            (trailing "/" in pattern assumed to be folder).
      --open                Open the *.sublime-project file. (automatic if no
                            arguments are given)
      --version             show program's version number and exit
