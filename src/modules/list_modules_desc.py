
MODULE_NAME = 'list-modules'
MODULE_DESC = 'List available modules'
MODULE_VER = '1.0'

def START(db, *args):
    """List modules found by python"""
    import sys
    
    modules = sys.modules['modules']._get_all_modules()
    mlist = modules.keys()
    mlist.sort()
    print
    for name in mlist:
        module = modules[name]
        print name, '-', module.MODULE_DESC, '[ version:', module.MODULE_VER, ']'
    print
