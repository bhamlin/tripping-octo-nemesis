
import MySQLdb as __M

__CONFIG = dict()

def load_config(path):
    import os
    conf_dir = os.path.abspath(os.path.expanduser(path))
    for filename in os.listdir(conf_dir):
        conf_file, _ = filename.split('.')
        CURRENT = dict()
        
        with open(os.path.join(conf_dir, filename), 'r') as fh:
            for line in fh:
                line = line.strip()
                
                if line.startswith('#') or line.startswith('//'):
                    line = None
                
                if line and ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip().lower()
                    value = value.strip()
                    
                    try:
                        value = int(value)
                    except:
                        pass
                    
                    CURRENT[key] = value
        if CURRENT:
            __CONFIG[conf_file] = CURRENT

def get(query, columns=None):
    _L = __CONFIG['login_darkstar']
    host = _L['mysql_host']
    port = _L['mysql_port']
    user = _L['mysql_login']
    passwd = _L['mysql_password']
    dbname = _L['mysql_database']
    pass
    db = __M.connect(host=host, port=port, user=user, passwd=passwd,
            db=dbname, conv={ __M.FIELD_TYPE.LONG: int })
    cur = db.cursor()
    
    cur.execute(query)
    if not columns:
        output = cur.fetchall()
    else:
        output = list()
        for row in cur.fetchall():
            output.append(dict(zip(columns, row)))
    
    cur.close()
    db.close()
    return output
