#! /usr/bin/python3
import os
import json
import sys, getopt
from steamcmd import steamcmd

cpath = r"config/cs2.json"
config = steamcmd.load_config(cpath)

serverdir = config['steamcmd']['options']['installDir']

def main(argv): # Runs user inputs and deploys functions
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
                InstallServer()
            else:
                print("Quitting...")
                sys.exit(2)
                
        case "validate":
            choice = input("Are you sure you would like to " +
                           "validate the server files?[y/n] ").lower()
            
            if choice == ("y") or choice == ("yes"):
                ValidateServer()
            else:
                print("Quitting...")
                sys.exit(2)
                
        case "update":
            choice = input("Are you sure you would like to " +
                           "update the server?[y/n] ").lower()
            
            if choice == ("y") or choice == ("yes"):
                UpdateServer()
            else:
                print("Quitting...")
                sys.exit(2)
                
        case "start":
            choice = input("Are you sure you would like to " +
                           "start the server?[y/n] ").lower()
            
            if choice == ("y") or choice == ("yes"):
                StartGame()
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
        
def ServerExist(): # Check if server is already installed.
    file_exist = os.path.exists(serverdir)
    if file_exist:
        print(f"Server is already installed. In order to update the server, " +
              "type this command: ./server.py -c update")
        sys.exit(2)
    else:
        return True
    
def InstallServer(): # Install game server only if dir /serverfiles/ does not exist.
    if ServerExist():
        steamcmd.update(cpath)
    
def UpdateServer(): # Updates the game server!
    print("Updating...")
    steamcmd.update(cpath)
    
def ValidateServer(): # Validate the game server!
    print("Validating game files!!!!")
    steamcmd.validate(cpath)
    
def StartGame(): # Start the game server!
    os.system(rf"{serverdir} -dedicated -usercon +map +game_type 0 +game_mode 1 "
              + f"+map de_dust2 +sv_setsteamaccount {config['cs2']['steamtoken']} +clientport 27015")
if __name__ == "__main__":
    main(sys.argv[1:])