#!/usr/bin/env python

import argparse
import os
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('output', help='Name of executable to create')
parser.add_argument('source', help='Path to find sources')

args = parser.parse_args()

IMG = os.path.abspath(args.output)

with open(IMG, 'w') as fh:
    fh.write('#!/usr/bin/env python\n')

os.chdir(args.source)

with zipfile.ZipFile(IMG, 'a', zipfile.ZIP_DEFLATED) as fh:
    for raw_path, _, names in os.walk('./'):
        if raw_path == '.':
            path = ''
        else:
            path = raw_path[2:]
        for name in names:
            file = os.path.join(path, name)
            fh.write(file)

os.chmod(IMG, 0755)
