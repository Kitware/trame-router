from trame.app import get_server
from trame.ui.html import DivLayout
from trame.ui.router import RouterViewLayout
from trame.widgets import html, router

server = get_server()
server.client_type = "vue3"
state, ctrl = server.state, server.controller

# ---------------------------------------------------------
# home
# ---------------------------------------------------------
with RouterViewLayout(server, "/", name="content"):
    html.Div("home - content")

with RouterViewLayout(server, "/", name="side"):
    html.Div("home - side")

# ---------------------------------------------------------
# foo
# ---------------------------------------------------------
with RouterViewLayout(server, "/foo", name="content"):
    html.Div("foo - content")

with RouterViewLayout(server, "/foo", name="side"):
    html.Div("foo - side")

# ---------------------------------------------------------
# bar
# ---------------------------------------------------------
with RouterViewLayout(server, "/bar", name="content"):
    html.Div("bar - content")

with RouterViewLayout(server, "/bar", name="side"):
    html.Div("bar - side")

# ---------------------------------------------------------
# Main UI
# ---------------------------------------------------------
with DivLayout(server) as layout:
    with html.Div("toolbar", style="border: solid 1px black;"):
        router.RouterLink("Home", to="/")
        router.RouterLink("Foo", to="/foo")
        router.RouterLink("Bar", to="/bar")

    with html.Div("side", style="border: solid 1px black;"):
        router.RouterView(name="side")

    with html.Div("content", style="border: solid 1px black;"):
        router.RouterView(name="content")

if __name__ == "__main__":
    server.start()
