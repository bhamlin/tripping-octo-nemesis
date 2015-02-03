
MODULE_NAME = 'list-sessions'
MODULE_DESC = 'List sessions active in the database'
MODULE_VER = '1.0'

def START(db, *args):
    """Remove Darkstar account sessions"""
    
    import argparse
    AP = argparse.ArgumentParser('ffxi-tools ' + MODULE_NAME,
            description='Lists active sessions')
    
    args = AP.parse_args(args=args)

    sessions = db.get('''
 select acc.login, c.charname
 from accounts_sessions sess
  left join accounts acc on sess.accid = acc.id
  left join chars c on sess.charid = c.charid
'''.strip(), ('login', 'character'))

    if sessions:
        print 'login            character'
        print '-----            ---------'
        for session in sessions:
            print '%-16s %s' % (session['login'], session['character'])
    else:
        print 'No sessions found'
