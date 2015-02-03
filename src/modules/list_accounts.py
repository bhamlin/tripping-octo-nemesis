
MODULE_NAME = 'list-accounts'
MODULE_DESC = 'List accounts on server'
MODULE_VER = '1.0'

def START(db, *args):
    """List FFXI accounts in the database"""
    print 'in', MODULE_NAME
