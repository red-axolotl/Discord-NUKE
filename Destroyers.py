import DiscordAPI
import time

class Nuke():
    def __init__(self, token: str, chID: int, guildID: int) -> None:
        self.API = DiscordAPI.Client(token)
        self.chID = chID
        self.guildID = guildID
        
    def Send(self, message: str):
        self.API.SendMessage(message, self.chID)
        channels = self.API.GetChannels(self.guildID)
        for channel in channels:
            self.API.SendMessage(message, channel["id"])
    
    def Start(self, message: str, count: int):
        for i in range(count):
            self.Send(message)
    
class Infinite():
    def __init__(self, token: str, chID: int, guildID: int) -> None:
        self.API = DiscordAPI.Client(token)
        self.chID = chID
        self.guildID = guildID
        
    def Send(self, message: str):
        self.API.SendMessage(message, self.chID)
        channels = self.API.GetChannels(self.guildID)
        for channel in channels:
            self.API.SendMessage(message, channel["id"])
    
    def Start(self, message: str):
        while True:
            self.Send(message)

class Renamer():
    def __init__(self, token: str, chID: int, guildID: int) -> None:
        self.API = DiscordAPI.Client(token)
        self.chID = chID
        self.guildID = guildID

    def Rename(self, name: str):
        channels = self.API.GetChannels(self.guildID)
        for channel in channels:
            self.API.RenameChannel(channel["id"], name)
            
    
    def Start(self, name: str):
        while True:
            self.Rename(name)