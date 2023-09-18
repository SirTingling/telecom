# json: https://docs.python.org/3/library/json.html
import json # Used to serialize and deserialize data sent over the WebSocket.
from channels.generic.websocket import AsyncWebsocketConsumer # Used to handle WebSocket connections.

class ChatroomWebSocketUser(AsyncWebsocketConsumer):
    """
    Handles WebSocket connections for chatrooms.
    """

    async def connect(self):
        """
        Establishes a WebSocket connection for a specific chatroom.
        """
        # Extract chatroom identifier from the URL route to the User.
        self.chatroom = self.scope['url_route']['kwargs']['chatroom']
        self.group_name = f'chatroom_group_{self.chatroom}'

        # Associate the current channel with the chatroom's group.
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        # Accept the WebSocket connection.
        await self.accept()

    async def disconnect(self, close_code):
        """
        Handles disconnection from the WebSocket.
        """
        # Disassociate the current channel from the chatroom's group.
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Processes a received WebSocket message.
        """
        # Deserialize the received message.
        received_data = json.loads(text_data)
        user_message = received_data['message']

        # Broadcast the message to the chatroom's group.
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'broadcast_message',
                'message': user_message
            }
        )

    async def broadcast_message(self, event):
        """
        Broadcasts the message to all members in the chatroom's group.
        """
        broadcasted_message = event['message']

        # Return the broadcasted message to the WebSocket.
        await self.send(text_data=json.dumps({
            'message': broadcasted_message
        }))
