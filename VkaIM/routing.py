from channels.routing import route, include
from account import consumers, views

websocket_routing = [
    route("websocket.receive", consumers.ws_message),
    route("websocket.connect", consumers.ws_connect),
    route("websocket.disconnect", consumers.ws_disconnect),
]


routing = [
    include(websocket_routing),
    # route("http.request", consumers.http_consumer),
    # route("http.request", views.visit_register, path=r'^register/$'),
    # route("http.request", views.do_register, path=r'^register/register.do'),
    # route("http.request", views.visit_login, path=r'^login/$'),
    # route("http.request", views.do_login, path=r'^login/login.do'),
]