from trame_router.widgets.router import *  # noqa: F403


def initialize(server):
    from trame_router import module

    server.enable_module(module)
