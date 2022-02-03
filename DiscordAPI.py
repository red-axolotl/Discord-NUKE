# import json
import requests

class Client:
    def __init__(self, token: str) -> None:
        self.token = token

    def SendMessage(self, text: str, id: str) -> bool:
        headers = {"authorization": self.token}
        payload = {"content": text}
        req = requests.post(f"https://discord.com/api/v9/channels/{id}/messages", data=payload, headers=headers)
        return True if req.status_code == 200 else False

    def RenameChannel(self) -> bool:
        return