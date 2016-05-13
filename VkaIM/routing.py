from channels.routing import route
from account import consumers

channel_routing = [
    # route("http.request", "account.consumers.http_consumer"),
    route("websocket.receive", consumers.ws_message),
    route("websocket.connect", consumers.ws_connect),
    route("websocket.disconnect", consumers.ws_disconnect),
]