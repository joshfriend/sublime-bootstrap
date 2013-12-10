#!/usr/bin/env python

import os
import sys
import subprocess
from subprocess import Popen, PIPE

from path import path


# The most common locations for Sublime Text
sublime_paths = {
    'win32': [
        'C:/Program Files (x86)/Sublime Text 2/sublime_text.exe',
        'C:/Program Files/Sublime Text 2/sublime_text.exe',
        'C:/Program Files (x86)/Sublime Text 3/sublime_text.exe',
        'C:/Program Files/Sublime Text 3/sublime_text.exe',
    ],
    'cygwin': [
        '/cygdrive/c/Program Files (x86)/Sublime Text 2/sublime_text.exe',
        '/cygdrive/c/Program Files/Sublime Text 2/sublime_text.exe',
        '/cygdrive/c/Program Files (x86)/Sublime Text 3/sublime_text.exe',
        '/cygdrive/c/Program Files/Sublime Text 3/sublime_text.exe',
    ],
    'darwin': [
        '/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl',
        '/Applications/Sublime Text 3.app/Contents/SharedSupport/bin/subl',
        '/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl',
    ],
}


def cygpath(path, *flags):
    """
    Wrapper for the cygpath utility
    """
    args = ['cygpath']
    args.extend(flags)
    args.append(str(path))

    shell = Popen(args,
                  stdout=PIPE,
                  stderr=PIPE,
                  shell=False,
                  universal_newlines=True)
    stdout, stderr = shell.communicate()
    if stderr:
        print stderr
        return None
    return stdout.replace('\\', '/').replace('\n', '')


def read_gitignore(path):
    with open(path, 'r') as gi:
        lines = gi.readlines()

    patterns = set()

    for line in lines:
        line = line.strip()
        if line:
            if line.startswith('#'):
                # Skip comment lines
                continue
            else:
                patterns.add(line)

    return list(patterns)


def get_git_root(path):
    args = ['git', 'rev-parse', '--show-toplevel']
    shell = Popen(args,
                  stdout=PIPE,
                  stderr=PIPE,
                  shell=False,
                  universal_newlines=True)
    stdout, stderr = shell.communicate()
    if stderr:
        print stderr
        return None
    return stdout.replace('\n', '')


def find_sublime():
    # Try to read cached path first
    try:
        p = open(path(__file__).parent / '.subl', 'r').read()
        return p
    except:
        pass

    # Go searching for sublime text
    try:
        paths = sublime_paths[sys.platform]
        for p in paths:
            if os.path.exists(p):
                # Save to cache file
                with open(path(__file__).parent / '.subl', 'w') as fp:
                    fp.write(p)
                return p
    except:
        pass
    return None


def find_sublime_project(git_root):
    for f in git_root.files():
        if f.isfile():
            if f.fnmatch('*.sublime-project'):
                return f
    return git_root / git_root.name + '.sublime-project'


def subl(*files):
    subl = find_sublime()

    if subl:
        if sys.platform == 'cygwin':
            # Run cygpath on file names to get windows equivalent paths
            files = [cygpath(f, '-w') for f in files]

        cmd = '"%s" %s' % (subl, ' '.join(files))
        subprocess.call(cmd, shell=True)
    else:
        print 'Could not find Sublime Text!'
