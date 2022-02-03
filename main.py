#!/bin/python3

import json
import grabber
import DiscordAPI

def NUKE():
    # TODO: implement NUKE
    return

def launch():
    listener = grabber.Grabber()
    listener.setup()
    message = listener.getMessage()
    text = message[0]
    chID = message[1]
    while True:
        if text == "run NUKE.exe":
            print("MATCH")
            break
        message = listener.getMessage()
        text = message[0]
        chID = message[1]
    cli = DiscordAPI.Client("ODc4MDU5NTUxNzA5MDg1Nzc3.Yeko3w.UAZRXV6s9xBDZ77miqHsgCRhOUU")
    cli.SendMessage("Acest server va fi bombardat!", chID)
    
    
if __name__ == '__main__':
    launch()