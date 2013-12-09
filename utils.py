#!/usr/bin/env python

from subprocess import Popen, PIPE


def _cygpath(path, *flags):
    """
    Wrapper for the cygpath utility
    """
    args = ['cygpath']
    args.extend(flags)
    args.append(path)

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
