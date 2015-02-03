#!/usr/bin/env python

import argparse
import sys

LIST_MODULES = 'list-modules'

AP = argparse.ArgumentParser('ffxi-tools',
        description='Tools for modifying the Darkstar database')
AP.add_argument('--config', '-c', default='/etc/darkstar/', metavar='PATH',
        help='Path for Darkstar config (Default: /etc/darkstar/)')
AP.add_argument('module', nargs='?',
        help='Module to use, or "%s" to see a list of available modules' % (LIST_MODULES))
AP.add_argument('options', nargs='*',
        help='Module options, or --help to get help on that module')

help = False
raw_args = list()
for arg in sys.argv[1:]:
    if arg.lower() in ('--help', '-h'):
        help = True
    else:
        raw_args.append(arg)
args = AP.parse_args(raw_args)

if not args.module:
    AP.print_help()
    exit()

import modules
import db

db.load_config(args.config)

if modules.has_module(args.module):
    module = modules.get_module(args.module)
    if help:
        module.START(db, '--help', *args.options)
    else:
        module.START(db, *args.options)
else:
    print 'Module named "%s" not found.' % (args.module)
