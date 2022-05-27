#!/bin/python3

import grabber
import Destroyers
import threading
import json

config = json.loads(open("config.json").read())

TOKEN = config["token"]
# WIDGET_URL = "https://discord.com/api/guilds/868198915105759242/widget.json"

def parse(message: list) -> None:
    text = str(message[0])
    chID = int(message[1])
    guildID = int(message[2])

    splittedText = text.split()
    print(f"Received a request for {splittedText[1]}!")

    if splittedText[1] == "NUKE.exe":
        arg = splittedText[2:]
        txt = ''
        for x in arg:
            txt += x
            txt += ' '

        nuke = Destroyers.Nuke(TOKEN, chID, guildID)
        nuke.Start(txt, 10)
    
    elif splittedText[1] == "Infinite.exe":
        arg = splittedText[2:]
        txt = ''
        for x in arg:
            txt += x
            txt += ' '

        infinite = Destroyers.Infinite(TOKEN, chID, guildID)
        infinite.Start(txt)

    elif splittedText[1] == "Renamer.exe":
        arg = splittedText[2:]
        txt = ''
        for x in arg:
            txt += x
            txt += ' '

        renamer = Destroyers.Renamer(TOKEN, chID, guildID)
        renamer.Start(txt)

    else:
        print(f"{splittedText[1]} not found!")

def launch() -> list:
    listener = grabber.Grabber(TOKEN)
    listener.setup()
    message = listener.getMessage()
    while True:
        if str(message[0]).startswith("run"):
            return message
        message = listener.getMessage()
    
    
if __name__ == '__main__':
    while True:
        message = launch()
        threading.Thread(target=parse, args=(message,)).start()
    # print(json.dumps(DiscordAPI.Client(TOKEN).GetChannels(863059333972754482), indent=4))