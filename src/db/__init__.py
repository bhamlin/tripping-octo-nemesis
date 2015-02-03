
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

def get(query):
    pass
