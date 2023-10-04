import os
import json

DEFAULT_CONFIG = {
    "steamcmd" :
    {
        "auth" :
        {
            "user" : "username",
            "pass" : "password"
        },
        "options" :
        {
            "login" : True,
            "appID" : 730,
            "installDir" : "/home/cs2/serverfiles/"
        }
    },
    "cs2" :
    {
        "steamtoken" : "STEAMTOKENHERE",
        "gameserverpath" : "/home/cs2/serverfiles/game/bin/linuxsteamrt64/cs2"
        
    }
}

def load_config(cpath): # Looks for config file, if not found then create a default one.
    try:
        with open(cpath) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file not found at {cpath}, creating a new one...")
        save_config(DEFAULT_CONFIG, cpath)
        return DEFAULT_CONFIG
    

def save_config(def_config, cpath):
    with open(cpath, 'w') as config_file:
        json.dump(def_config, config_file, indent=4)

def update(cpath): # Update CS:2 Server with steamcmd.
    config = load_config(cpath) 
    steamcmd = config['steamcmd']
    options = steamcmd['options']
    
    if options['login']:
        os.system(f"steamcmd +force_install_dir {options['installDir']} +login {steamcmd['auth']['user']} {steamcmd['auth']['pass']} +app_update {options['appID']} +quit")
    elif not options['login']:
        try:
            os.system(f"steamcmd +force_install_dir {options['installDir']} +login anonymous +app_update {options['appID']} +quit")
        except:
            print("Game server probably needs a login, change cs2.json.")
            
def validate(cpath): #Validates the cs2 server.
    config = load_config(cpath) 
    steamcmd = config['steamcmd']
    options = steamcmd['options']
    
    if options['login']:
        os.system(f"steamcmd +force_install_dir {options['installDir']} +login {steamcmd['auth']['user']} {steamcmd['auth']['pass']} +app_update {options['appID']} validat +quit")
    elif not options['login']:
        try:
            os.system(f"steamcmd +force_install_dir {options['installDir']} +login anonymous +app_update {options['appID']} validate +quit")
        except:
            print("Game server probably needs a login, change cs2.json.")
