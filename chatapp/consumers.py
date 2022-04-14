from channels.generic.websocket import AsyncJsonWebsocketConsumer, AsyncWebsocketConsumer
import json
from django.contrib.auth import get_user_model

User = get_user_model()
class PublicChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
            print("PublicChatConsumer: connect: " + str(self.scope['user']))
            await self.accept()

    async def disconnect(self, code):
        print("PublicChatConsumer: disconnect")

    async def receive_json(self, content):
        command = content.get("command", None)
        print("PublicChatConsumer: receive_json" + str(command))

        