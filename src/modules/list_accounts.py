
MODULE_NAME = 'list-accounts'
MODULE_DESC = 'List accounts on server'
MODULE_VER = '1.0'

def START(db, *args):
    """List FFXI accounts in the database"""
    
    logins = db.get('select id, login from accounts', ('id', 'name'));

    if logins:
        print 'id\tname'
        print '----\t----'
        for login in logins:
            print '%s\t%s' % (login['id'], login['name'])
