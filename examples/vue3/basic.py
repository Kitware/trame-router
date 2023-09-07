r"""
Version for trame 1.x - https://github.com/Kitware/trame/blob/release-v1/examples/PlainPython/Router/app.py
Delta v1..v2          - https://github.com/Kitware/trame/commit/f2ad3e65c17539315d23f5e3e981048f68b4d31e

Installation requirements:
    pip install trame trame-vuetify trame-router
"""

from trame.app import get_server
from trame.ui.vuetify3 import SinglePageWithDrawerLayout
from trame.ui.router import RouterViewLayout
from trame.widgets import router, vuetify3 as vuetify

server = get_server()
server.client_type = "vue3"
state, ctrl = server.state, server.controller

# Home route
with RouterViewLayout(server, "/"):
    with vuetify.VCard():
        vuetify.VCardTitle("This is home")

# Foo route
with RouterViewLayout(server, "/foo"):
    with vuetify.VCard():
        vuetify.VCardTitle("This is foo")
        with vuetify.VCardText():
            vuetify.VBtn("Take me back", click="$router.back()")

# Bar/id
with RouterViewLayout(server, "/bar/:id"):
    with vuetify.VCard():
        vuetify.VCardTitle("This is bar with ID '{{ $route.params.id }}'")

# Main page content
with SinglePageWithDrawerLayout(server) as layout:
    layout.title.set_text("Multi-Page demo")

    with layout.content:
        with vuetify.VContainer():
            router.RouterView()

    # add router buttons to the drawer
    with layout.drawer:
        with vuetify.VList(
            shaped=True,
            v_model=("selectedRoute", 0),
            v_model_opened=("open", []),
            __properties=[("v_model_opened", "v-model:opened")],
        ) as c:
            vuetify.VListSubheader("Routes")

            vuetify.VListItem(to="/", prepend_icon="mdi-home", title="Home")
            vuetify.VListItem(to="/foo", prepend_icon="mdi-food", title="Foo")

            vuetify.VListSubheader("Bars")
            vuetify.VListItem(
                v_for="id in 3",
                key="id",
                to=("`/bar/${id}`",),
                prepend_icon="mdi-peanut-outline",
                title=("`Bar: Id ${id}`",),
            )

        print(c)

if __name__ == "__main__":
    server.start()
