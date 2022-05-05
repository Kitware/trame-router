import json
from trame_client.widgets.core import AbstractElement
from trame_router import module

APP_ROUTES = {}
CHAR_TO_CONVERT = " .-"

STATE_ROUTES_KEY = "trame__routes"


def slugify(name):
    for specialChar in CHAR_TO_CONVERT:
        name = name.replace(specialChar, "_")
    return name


def flush_routes(app):
    app_key = slugify(app.name)
    data = APP_ROUTES[app_key]
    routes = []

    for path, components in data.items():
        # container = {}
        # routes.append({ "path": path, "components": container })
        # for name, template in components.items():
        #     container[name] = { "template": template }
        routes.append(
            {"path": path, "component": {"template": components.get("default")}}
        )

    app.state[STATE_ROUTES_KEY] = routes


def register_route(app, name, path, component):
    global APP_ROUTES
    app_key = slugify(app.name)
    APP_ROUTES.setdefault(app_key, {})
    APP_ROUTES[app_key].setdefault(path, {})
    APP_ROUTES[app_key][path][name] = component
    flush_routes(app)


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(module)


class RouterLink(HtmlElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("router-link", children, **kwargs)
        self._attr_names += [
            "to",
            "replace",
            "append",
            "tag",
            "active_class",
            "exact",
            "exact_path",
            "exact_path_active_class",
            "event",
            "exact_active_class",
            "aria_current_value" "custom",
        ]


class RouterView(HtmlElement):
    def __init__(self, children=None, name="default", **kwargs):
        super().__init__("router-view", children, **kwargs)
        self._attr_names += [
            "name",
            "mode",
            "base",
            ("link_active_class", "linkActiveClass"),
            ("link_exact_active_class", "linkExactActiveClass"),
            ("scroll_behavior", "scrollBehavior"),
            ("parse_query", "parseQuery"),
            "fallback",
        ]
        self.server.state.setdefault(STATE_ROUTES_KEY, [])
