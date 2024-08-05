trame-router brings multi-page navigation to trame
===========================================================================

.. image:: https://github.com/Kitware/trame-router/actions/workflows/test_and_release.yml/badge.svg
    :target: https://github.com/Kitware/trame-router/actions/workflows/test_and_release.yml
    :alt: Test and Release

Trame-router extend trame **widgets** and **ui** with **Vue Router** components and helper to streamline its usage with trame.
Vue Router is the official router for Vue.js on which trame is based.


Installing
-----------------------------------------------------------

trame-router can be installed with `pip <https://pypi.org/project/trame-router/>`_:

.. code-block:: bash

    pip install --upgrade trame-router


Usage
-----------------------------------------------------------

The `Trame Tutorial <https://kitware.github.io/trame/docs/tutorial.html>`_ is the place to go to learn how to use the library and start building your own application.

The `API Reference <https://trame.readthedocs.io/en/latest/index.html>`_ documentation provides API-level documentation.

`The original Vue Router documentation <https://router.vuejs.org/>`_ provide a great introduction resource.

The router elements can be used as follow in trame:

.. code-block:: python

    # [...]
    from trame.ui.router import RouterViewLayout
    from trame.widgets import router

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

Environment variables
-----------------------------------------------------------

With vue3 and docker, trame-router can leverage the html5 history mode but by default we use the "hash" mode.
To enable it, you need to define a **TRAME_ROUTER_HISTORY_MODE** environment variable that should either be set to "html5" or "hash".
This can only work if using our docker bundle or with a proper web server configuration when delivering the static HTML/JS/CSS content yourself.


License
-----------------------------------------------------------

trame-router is made available under the MIT License. For more details, see `LICENSE <https://github.com/Kitware/trame-router/blob/master/LICENSE>`_
This license has been chosen to match the one use by `Vue Router <https://github.com/vuejs/router/blob/main/LICENSE>`_ which is used under the cover.


Community
-----------------------------------------------------------

`Trame <https://kitware.github.io/trame/>`_ | `Discussions <https://github.com/Kitware/trame/discussions>`_ | `Issues <https://github.com/Kitware/trame/issues>`_ | `RoadMap <https://github.com/Kitware/trame/projects/1>`_ | `Contact Us <https://www.kitware.com/contact-us/>`_

.. image:: https://zenodo.org/badge/410108340.svg
    :target: https://zenodo.org/badge/latestdoi/410108340


Enjoying trame?
-----------------------------------------------------------

Share your experience `with a testimonial <https://github.com/Kitware/trame/issues/18>`_ or `with a brand approval <https://github.com/Kitware/trame/issues/19>`_.
