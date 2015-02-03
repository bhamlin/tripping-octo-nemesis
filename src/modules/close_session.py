
MODULE_NAME = 'close-session'
MODULE_DESC = "Remove an account's session"
MODULE_VER = '1.0'

def START(db, *args):
    """Remove Darkstar account sessions"""
    
    import argparse
    AP = argparse.ArgumentParser('ffxi-tools ' + MODULE_NAME,
            description='Removes a session')
    AP.add_argument('login', metavar='login_name',
            help='The login for the account')
    
    args = AP.parse_args(args=args)
    
    sessions = db.get('''
 select acc.login, c.charname
 from accounts_sessions sess
  left join accounts acc on sess.accid = acc.id
  left join chars c on sess.charid = c.charid
'''.strip(), ('login', 'character'))

    if sessions and args.login in str(sessions):
        print 'Removing session for', args.login, '...',
        
        db.run('''
     delete from accounts_sessions
     where accid = (select id from accounts where login = '%s')
    '''.strip() % (args.login,))
        
        print 'Removed'
    else:
        print 'No session found for account', args.login
