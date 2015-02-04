
MODULE_NAME = 'set-position'
MODULE_DESC = 'Move a character to its homepoint, or to another set location'
MODULE_VER = '1.0'

def START(db, *args):
    """Remove Darkstar account sessions"""
    
    class Position(object):
        def __init__(self, rot, x, y, z, zone):
            self.rot = rot
            self.x = x
            self.y = y
            self.z = z
            self.zone = zone
    
    NATIONS = ['sandoria', 'bastok', 'windurst']

    LOCATIONS = {
        NATIONS[0]: Position( 18,  151.910, -2.212, 156.489, 230),
        NATIONS[1]: Position( 63, -189.633, -8.000, -25.075, 235),
        NATIONS[2]: Position( 38,  -95.999, -5.001,  63.763, 241),
        'jeuno':    Position(176,  339.849, 20.522, 583.528, 110),
        # LOL
        'jormungand': Position(220, -203.895, -175.281, 144.767, 5),
    }
    
    CHOICES = ['home', 'by-nation']
    CHOICES += LOCATIONS.keys()

    import argparse
    AP = argparse.ArgumentParser('ffxi-tools ' + MODULE_NAME,
            description='Move a character to its homepoint, or to another set location')
    AP.add_argument('character', metavar='character_name',
            help='The character to move')
    AP.add_argument('location', metavar='location', choices=CHOICES, default=CHOICES[0],
            help='Locations must be one of: "%s".  Default is "%s".'
                % ('", "'.join(CHOICES), CHOICES[0]))
    
    args = AP.parse_args(args=args)
    
    charid = db.get(''' select charid, charname from chars where lower(charname) = '%s' '''
            % (args.character.lower(),))
    
    if not charid:
        print 'No character found by name', args.character
        return
    else:
        charname = charid[0][1]
        charid = charid[0][0]
    
    session = db.get(''' select charid from accounts_sessions sess where charid = %s '''.strip()
            % (charid,))

    if session:
        print 'Character', charname, 'has a current session, not modifying position'
        return
    
    # If there is a character with that name,
    # and no existing session for that character,
    # proceed with the move
    location = CHOICES[0]
    
    if args.location == CHOICES[1]:
        nationid = int((db.get(''' select nation from chars where charid = '%s' '''
                % (charid,)))[0][0])
        if nationid > len(NATIONS):
            print 'Unknown nation value', nationid
            return
        location = NATIONS[nationid]
    else:
        location = args.location
    
    if location == 'home':
        sql = ''' update chars set pos_rot=home_rot, pos_zone=home_zone,
                    pos_x=home_x, pos_y=home_y, pos_z=home_z where charid = %s
               '''.strip() % (charid,)
        db.run(sql)
        print charname, 'sent to home point'
    elif location in CHOICES[2:]:
        pos = LOCATIONS[location]
        sql = ''' update chars set pos_rot=%s, pos_zone=%s,
                    pos_x=%s, pos_y=%s, pos_z=%s where charid = %s
               '''.strip() % (pos.rot, pos.zone, pos.x, pos.y, pos.z, charid,)
        db.run(sql)
        print charname, 'sent to', location
    else:
        # How did you even get here?
        print 'There is no', args.location
