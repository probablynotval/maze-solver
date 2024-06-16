import os

import rtoml


def get_input(prompt, default=None, itype=None):
    while True:
        user_input = input(f"{prompt} [{default}]: ").strip()
        if not user_input and default is not None:
            return default
        if itype == bool:
            if user_input.lower() in ("y", "yes"):
                return True
            elif user_input.lower() in ("n", "no"):
                return False
            else:
                print("Please enter 'Y' or 'N'.")
        try:
            value = itype(user_input)
            return value
        except ValueError:
            print("Please enter a valid integer.")


def generate_config():
    print("Enter configuration values (press Enter for default value in brackets)...")
    window_width = get_input("Window width", default=800, itype=int)
    window_height = get_input("Window height", default=600, itype=int)
    rows = get_input("Rows", default=10, itype=int)
    columns = get_input("Columns", default=10, itype=int)
    size_x = get_input("Cell size x", default=50, itype=int)
    size_y = get_input("Size Y", default=50, itype=int)
    vnc = get_input("Set up a VNC server?", default=False, itype=bool)

    config = {
        "window": {
            "width": window_width,
            "height": window_height,
        },
        "grid": {
            "rows": rows,
            "columns": columns,
            "size_x": size_x,
            "size_y": size_y,
        },
        "vnc": {
            "bool": vnc,
        },
    }

    with open("config.toml", "w") as file:
        file.write(rtoml.dumps(config))

    print("TOML configuration file 'config.toml' generated successfully.")


def load_config():
    if os.path.exists("config.toml"):
        with open("config.toml", "r") as file:
            config = rtoml.load(file)
        return config
    else:
        raise FileNotFoundError("config.toml not found.")


def get_config():
    if not os.path.exists("config.toml"):
        print("Configuration file 'config.toml' does not exist. Generating...")
        generate_config()
    return load_config()
