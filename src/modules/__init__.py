
import pkgutil as __p
import sys as __s

__self = __s.modules['modules'] # Find self; very zen

__available = dict()

def _get_all_modules():
    """Return all modules found"""
    return __available

def get_module(name):
    """Return the named module"""
    return __available[name]

def has_module(name):
    """Returns True if module exists"""
    return name in __available

# Harrass python into finding all submodules of the module 'modules'
for _, modname, ispkg in __p.iter_modules(__self.__path__):
    # Attempt to import the found module
    q = __import__('modules.' + modname, globals(), locals(),
        ['MODULE_NAME', 'MODULE_DESC', 'MODULE_VER'], -1)
    # If it's one of our modules we've found...
    if 'MODULE_NAME' in dir(q) and q.MODULE_NAME:
        if 'MODULE_DESC' in dir(q) and 'MODULE_VER' in dir(q):
            # Add it to the list of available ones
            __available[q.MODULE_NAME] = q

del modname
del ispkg
del q
