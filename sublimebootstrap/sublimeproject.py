#!/usr/bin/env python

import json
import os

from path import path


class SublimeProject:
    def __init__(self, f):
        self.path = path(f)
        try:
            with open(self.path, 'r') as spf:
                self._data = json.load(spf)
        except:
            with open(path(__file__).dirname() / 'data/template.sublime-project', 'r') as spf:
                self._data = json.load(spf)


    def __getitem__(self, k):
        return self._data[k]


    def __setitem__(self, k, v):
        self._data[k] = v


    def save(self):
        with open(self.path, 'w') as spf:
            json.dump(self._data, spf, indent=4, sort_keys=True)


    def ignore_files(self, *files):
        for folder in self['folders']:
            try:
                patterns = set(folder['file_exclude_patterns'])
                patterns.update(files)
                folder['file_exclude_patterns'] = list(patterns)
            except KeyError:
                folder['file_exclude_patterns'] = files


    def ignore_folders(self, *folders):
        for folder in self['folders']:
            try:
                patterns = set(folder['folder_exclude_patterns'])
                patterns.update([f.rstrip('/') for f in folders])
                folder['folder_exclude_patterns'] = list(patterns)
            except KeyError:
                folder['folder_exclude_patterns'] = [f.rstrip('/') for f in folders]


    def add_folders(self, *folders):
        for folder in folders:
            folder = os.path.relpath(folder, self.path.dirname())
            print folder
            try:
                # Copy settings from an existing folder
                self['folders'].append(self['folders'][0])

                # Correct the path name
                self['folders'][-1]['path'] = folder
            except:
                self['folders'].append({
                    'path': folder,
                    'file_exclude_patterns': [],
                    'folder_exclude_patterns': []
                })
