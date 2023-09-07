from pathlib import Path

# Compute local path to serve
serve_path = str(Path(__file__).with_name("vue3").resolve())

# Serve directory for JS/CSS files
serve = {"__trame_router3": serve_path}

# List of JS files to load (usually from the serve path above)
scripts = ["__trame_router3/trame-router.umd.js"]

# List of Vue plugins to install/load
vue_use = ["trame_router"]
