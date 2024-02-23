from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        return self.accept()
    
    async def disconnect(self, code):
        return await super().disconnect(code)
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        response = {
            'status': 'Message sent successfully'
        }
        await self.send(json.dumps(response))