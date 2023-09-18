# Django Channels imports to handle routing and middleware.
from channels.routing import ProtocolTypeRouter, URLRouter # Import the ProtocolTypeRouter and URLRouter classes from channels.routing
from channels.auth import AuthMiddlewareStack # Import the authentication middleware stack
# ----------------------------------------------------------------------------------------------------------------------------------- >>
# Local import for chat app's routing definitions.
import chatroom.routing
# ----------------------------------------------------------------------------------------------------------------------------------- >>
# Application's routing definition.
# It is responsible for directing incoming protocol types to the correct application handling.
application_routing = {
    # For WebSocket protocol type, it wraps the routing inside an authentication middleware.
    # This ensures only authenticated users can connect via WebSockets.
    'websocket': AuthMiddlewareStack(
        URLRouter(chatroom.routing.websocket_routes)
    ),
}
# ----------------------------------------------------------------------------------------------------------------------------------- >>
# Instantiate the application with the defined routing.
application = ProtocolTypeRouter(application_routing)