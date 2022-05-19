from trame_router.widgets.router import *


def initialize(server):
    from trame_router import module

    server.enable_module(module)
