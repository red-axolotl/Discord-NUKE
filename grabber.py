import websocket
import json
import threading
import time

class Grabber:
    def __init__(self, token) -> None:
        self.token = token

    def send_json_request(self, request:dict):
        self.ws.send(json.dumps(request))

    def recieve_json_response(self):
        response = self.ws.recv()
        if response:
            return json.loads(response)

    def heartbeat(self):
        print("Heartbeat begin")
        while True:
            time.sleep(self.heartbeat_interval)
            heartbeatJSON = {
                "op": 1,
                "d": "null"
            }
            self.send_json_request(heartbeatJSON)
            print("Hartbeat sent")

    def setup(self) -> websocket.WebSocket:
        self.ws = websocket.WebSocket()
        self.ws.connect("wss://gateway.discord.gg/?v=6&encording=json")
        event = self.recieve_json_response()
        self.heartbeat_interval = event["d"]["heartbeat_interval"] / 1000
        print(f"Heartbeat: {self.heartbeat_interval}")
        heart = threading.Thread(target=self.heartbeat)
        heart.start()

    def getMessage(self) -> list:


        header = {
            "authorization": self.token,
            }

        payload = {
            "op": 2,
            "d": {
                "token": self.token,
                "properties": {
                    "$os": "windows",
                    "$browser": "chrome",
                    "$device": "pc"
                }
            }
        }

        self.send_json_request(payload)

        try:
            while True:
                event = self.recieve_json_response()
                try:
                    if event["d"]["content"]:
                        return [event["d"]["content"], event["d"]["channel_id"], event["d"]["guild_id"]]
                except:
                    pass
        except:
            print("Closed listener")
