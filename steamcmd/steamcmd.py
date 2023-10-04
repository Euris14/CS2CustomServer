""" This is my way of using steamcmd with python. """
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
    """ Looks for the default config file, if one can not be found
    then it creates a new one. """
    try:
        with open(cpath) as config:
            return json.load(config)
    except FileNotFoundError:
        print(f"Config file not found at {cpath}, creating a new one...")
        save_config(DEFAULT_CONFIG, cpath)
        return DEFAULT_CONFIG
def save_config(def_config, cpath):
    """ This function saves the new default config to the default config dir """
    with open(cpath, 'w') as config_file:
        json.dump(def_config, config_file, indent=4)
def update(cpath): # Update CS:2 Server with steamcmd.
    """ Updates or installs server using steamcmd. """
    config = load_config(cpath)
    steamcmd = config['steamcmd']
    options = steamcmd['options']
    if options['login']:
        os.system(f"steamcmd +force_install_dir {options['installDir']} " +
                  f"+login {steamcmd['auth']['user']} " +
                  f"{steamcmd['auth']['pass']} +app_update {options['appID']} +quit")
    elif not options['login']:
        try:
            os.system(f"steamcmd +force_install_dir {options['installDir']} +login anonymous " +
                      f"+app_update {options['appID']} +quit")
        except:
            print("Game server probably needs a login, change cs2.json.")
def validate(cpath): #Validates the cs2 server.
    """ **** Validates serverdir against steam default files and replaces them (I think?)"""
    config = load_config(cpath)
    steamcmd = config['steamcmd']
    options = steamcmd['options']
    if options['login']:
        os.system(f"steamcmd +force_install_dir {options['installDir']} " +
                  f"+login {steamcmd['auth']['user']} {steamcmd['auth']['pass']} " +
                  f"+app_update {options['appID']} validate +quit")
    elif not options['login']:
        try:
            os.system(f"steamcmd +force_install_dir {options['installDir']} +login anonymous" +
                      f" +app_update {options['appID']} validate +quit")
        except:
            print("Game server probably needs a login, change cs2.json.")
