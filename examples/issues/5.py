from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout
from trame.ui.router import RouterViewLayout
from trame.widgets import router
from trame.widgets import vuetify3
import pyvista as pv
from pyvista.trame.ui import plotter_ui

server = get_server(client_type="vue3")
state, ctrl = server.state, server.controller

with SinglePageLayout(server, full_height=True) as layout:
    with layout.content:
        with vuetify3.VContainer(
            fluid=True,
            classes="pa-0 fill-height",
        ):
            router.RouterView()


with RouterViewLayout(server, "/") as layout:
    # use the full parent size
    layout.root.style = "width: 100%; height: 100%;"

    pl_home = pv.Plotter(off_screen=True)
    sphere = pv.Sphere()
    pl_home.add_mesh(sphere, color="blue", name="sphere")

    view = plotter_ui(pl_home, mode="trame")
    ctrl.view_update = view.update
    ctrl.view_update_image = view.update_image
    ctrl.reset_camera = view.reset_camera

if __name__ == "__main__":
    server.start()
