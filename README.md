# Sublime Bootstrap
===================

A small program to easily set up a Sublime Text project file.

## Installation

## Usage

View the help for this tool by executing the following command in a shell:

    $ sbs -h
    usage: sbs [-h] [-if IGNORED_FILES] [-id IGNORED_FOLDERS]
               [-ad ADD_DIRS] [--import-gitignore]
               [--import-system-gitignore] [--install-subl]
               [name]

    Bootstrap app for Sublime projects.

    positional arguments:
      name                  Name of the sublime config file (default is
                            <repo_root_dir_name>.sublime-project if a *.sublime-
                            project file cannot be found in the repo root).

    optional arguments:
      -h, --help            show this help message and exit
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
      --install-subl        Install the "subl" command line tool.

