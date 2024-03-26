from trame.app import get_server
from trame.ui.vuetify3 import SinglePageWithDrawerLayout
from trame.ui.router import RouterViewLayout
from trame.widgets import router, vuetify3 as vuetify

server = get_server()
server.client_type = "vue3"
state, ctrl = server.state, server.controller

# def adjust_route(entry):
#     if len(entry.get("components", {})) == 1:
#         component = list(entry.get("components", {}).values())[0]
#         new_entry = { **entry, "component": component }
#         new_entry.pop("components")
#         return new_entry
#     return entry

# @ctrl.add("on_server_ready")
# def on_ready(trame__routes, **kwargs):
#     import json
#     for key in kwargs:
#         if key.startswith("trame__template"):
#             print(key)
#             print("-"*60)
#             print(kwargs[key])
#             print("-"*60)

#     # state.trame__routes = [adjust_route(route) for route in state.trame__routes]
#     print(json.dumps(state.trame__routes, indent=2))


with RouterViewLayout(server, "/"):
    with vuetify.VCard():
        vuetify.VCardTitle("This is home")

with RouterViewLayout(server, "/foo"):
    with vuetify.VCard():
        vuetify.VCardTitle("This is foo")

with RouterViewLayout(server, "/bar/:id"):
    with vuetify.VList():
        vuetify.VListItem("Bar {{ $route.params.id }} item 1")
        vuetify.VListItem("Bar {{ $route.params.id }} item 2")
        vuetify.VListItem("Bar {{ $route.params.id }} item 3")

with SinglePageWithDrawerLayout(server) as layout:
    with layout.toolbar:
        vuetify.VBtn("Home", to="/")
        vuetify.VBtn("Foo", to="/foo")
        vuetify.VBtn("Bar 1", to="/bar/1")
        vuetify.VBtn("Bar 2", to="/bar/2")
        vuetify.VBtn("Bar 3", to="/bar/3")

    with layout.content:
        router.RouterView()

    # print(layout)

if __name__ == "__main__":
    server.start()
