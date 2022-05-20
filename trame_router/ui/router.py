from trame_client.ui.core import AbstractLayout
from trame_client.widgets.html import Div
from trame_client.widgets.trame import ServerTemplate
from trame_router.widgets.router import register_route

CHAR_TO_CONVERT = "/-:*"


def path_to_name(path: str):
    name = path
    for specialChar in CHAR_TO_CONVERT:
        name = name.replace(specialChar, "_")
    return name


class RouterViewLayout(AbstractLayout):
    """
    Layout to be used for defining content of a given route

    :param _server: Server on which to be bound
    :param path: Route path to be linked to ('/foo' or '/bar/:id')
    :param name: Name for that path. (default: 'default')
    """
    def __init__(self, _server, path, name="default", **kwargs):
        template_name = path_to_name(path)
        register_route(
            _server,
            name,
            path,
            ServerTemplate(trame_server=_server, name=template_name).html,
        )
        super().__init__(
            _server,
            Div(trame_server=_server, **kwargs),
            template_name=template_name,
            **kwargs,
        )


__all__ = [
    "RouterViewLayout",
]
