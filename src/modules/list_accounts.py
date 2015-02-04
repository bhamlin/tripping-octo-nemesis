
MODULE_NAME = 'list-accounts'
MODULE_DESC = 'List accounts on server'
MODULE_VER = '1.0'

def START(db, *args):
    """List FFXI accounts in the database"""
    
    import argparse
    AP = argparse.ArgumentParser('ffxi-tools ' + MODULE_NAME,
            description='Lists accounts')
    
    args = AP.parse_args(args=args)

    logins = db.get('select id, login from accounts order by login', ('accid', 'login'));

    if logins:
        print 'accid            login'
        print '-----            -----'
        for login in logins:
            print '%-16s %s' % (login['accid'], login['login'])
    else:
        print 'No accounts found'
