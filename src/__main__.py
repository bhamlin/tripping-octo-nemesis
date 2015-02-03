#!/usr/bin/env python

import argparse

LIST_MODULES = 'list-modules'

AP = argparse.ArgumentParser()
AP.add_argument('--config', '-c', default='/etc/darkstar/conf/', metavar='PATH',
        help='Path for Darkstar config (Default: /etc/darkstar/conf/)')
AP.add_argument('module', nargs='?',
        help='Module to use, or "%s" to see a list of available modules' % (LIST_MODULES))
AP.add_argument('options', nargs='*',
        help='Module options, or --help to get help on that module')

args = AP.parse_args()

if not args.module:
    AP.print_help()
    exit()

import modules
import db

db.load_config(args.config)

if modules.has_module(args.module):
    module = modules.get_module(args.module)
    module.START(db, *args.options)
else:
    print 'Module named "%s" not found.' % (args.module)
