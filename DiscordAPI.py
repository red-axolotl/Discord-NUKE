import json
import requests

class Client:
    def __init__(self, token: str) -> None:
        self.token = token

    def SendMessage(self, text: str, id: str) -> bool:
        headers = {"authorization": self.token}
        payload = {"content": text}
        req = requests.post(f"https://discord.com/api/v9/channels/{id}/messages", data=payload, headers=headers)
        return True if req.status_code == 200 else False

    def GetChannels(self, guildID: int) -> dict:
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.token
            }
        req = requests.get(f"https://discord.com/api/v9/guilds/{guildID}/channels", headers=headers)
        return req.json()

    def RenameChannel(self, channelID: int, name: str) -> bool:
        name.replace(' ', '-')
        illegal = "`~!@#$%^&*()+={}[]:;\"\'|\\<,>.?/"
        for char in illegal:
            name.replace(char, '')

        headers = {
            "Authorization": self.token
        }
        data = {
            "name": name
        }
        
        return "retry_after" not in requests.patch(f"https://discord.com/api/v9/channels/{channelID}", json=data, headers=headers).json().keys()