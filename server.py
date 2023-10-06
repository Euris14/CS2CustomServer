#! /usr/bin/python3.10
"""Controls cs2 server"""
import os
import sys
import getopt
#import subprocess
from steamcmd import steamcmd

USR_DIR = os.path.expanduser('~')
CONFIG_PATH = r"config/cs2.json"
CONFIG = steamcmd.load_config(CONFIG_PATH)

serverdir = CONFIG['steamcmd']['options']['installDir']
SERVERDIR = serverdir.replace("~", USR_DIR)
SERVER = CONFIG['server']
LAUNCHSERVER = SERVER['gameserverpath'].replace("~", USR_DIR)

def main(argv): # Runs user inputs and deploys functions
    """ This is the main function, which runs all functions and collects """
    """ user input. """
    """ Arg: argv | user input from ./server -c"""
    choice = ''
    opts, args = getopt.getopt(argv, "hc:",["choice="])
    for opt, arg in opts: # gets command and argument.
        if opt == '-h':
            print('server.py -c <choice>')
            sys.exit(5)
        elif opt in ('-c', "--choice"):
            choice = arg
    match choice.lower(): # Check user input.
        case "install":
            choice = input("Are you sure you would like to " +
                           "install?[y/n] ").lower()
            if choice == ("y") or choice == ("yes"):
                install_server()
            else:
                print("Quitting...")
                sys.exit(2)
        case "validate":
            print("Be cautious with this on as it can rewrite some custom server files!")
            choice = input("Are you sure you would like to " +
                           "validate the server files?[y/n] ").lower()
            if choice == ("y") or choice == ("yes"):
                validate_server()
            else:
                print("Quitting...")
                sys.exit(2)
        case "update":
            choice = input("Are you sure you would like to " +
                           "update the server?[y/n] ").lower()
            if choice == ("y") or choice == ("yes"):
                update_server()
            else:
                print("Quitting...")
                sys.exit(2)
        case "start":
            choice = input("Are you sure you would like to " +
                           "start the server?[y/n] ").lower()
            if choice == ("y") or choice == ("yes"):
                start_server()
            else:
                print("Quitting...")
                sys.exit(2)
        case _: # Displays valid functions, if none inputed.
            print('./server.py -c <choice>')
            functions = ['install', 'update', 'validate', 'start']
            print("Choices:")
            for i in range(len(functions)):
                print(f"{i + 1}. ./server.py -c {functions[i]}")
            sys.exit(5)
def file_exist(serverdir): # Check if server is already installed.
    """ This function checks the serverdir for an existing server. """
    file_exist = os.path.exists(serverdir)
    if file_exist:
        return True
    return False
def install_server(): # Install game server only if dir /serverfiles/ does not exist.
    """ This function installs the server to the server
        path listed in the config file."""
    if not file_exist(SERVERDIR):
        steamcmd.update(CONFIG_PATH)
    else:
        print("Server is already installed. In order to update the server, " +
              "type this command: ./server.py -c update")
        sys.exit(2)
        
    
def update_server():# Updates the game server!
    """ This function updates the server. """
    print("Updating...")
    steamcmd.update(CONFIG_PATH)
def validate_server():
    """ This function validates the server paths and changes each one back
    to the server original. """
    print("Validating game files!!!!")
    steamcmd.validate(CONFIG_PATH)
def start_server():
    """ This function starts the server in this case its cs2. """
    if file_exist(fr'{USR_DIR}/serverfiles/game/csgo/cfg/server.cfg'):
        os.system(f"{LAUNCHSERVER} -dedicated -insecure -usercon +map +game_type " +
                    f"{SERVER['gametype']} +game_mode {SERVER['gamemode']} " +
                    f"+map {SERVER['map']} +sv_setsteamaccount {SERVER['steamtoken']} "+
                    f"+clientport {SERVER['port']}")
    else:
        print("Making default server.cfg!")
        try:
            os.system(f"cp {USR_DIR}/CS2CustomServer/config/default/server.cfg {USR_DIR}/serverfiles/game/csgo/cfg/")
        except Exception as a:
            return a
        print("Done. \nPlease re-run the command.")
        
if __name__ == "__main__":
    main(sys.argv[1:])
