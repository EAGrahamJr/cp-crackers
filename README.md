# A Personal Circuit Python Library

This is just stuff I dorked up in various ways and don't want to repeat myself.

Use at your own risk.

## Dependencies

The `cp-crackers` package does not install Adafruit dependencies for consumers.
Install the libraries needed for the modules you use. For desktop development
of this project, the default `dev` dependency group installs them so the editor
can resolve their imports:

```sh
uv sync
```

Select this project's `.venv` interpreter in VS Code. Consumers do not receive
the development group. Blinka and the hardware-dependent libraries require
supported hardware to run.

| Package | Imports needed | Desktop distributions |
| --- | --- | --- |
| `movement` | `adafruit_motor` and `digitalio` | `adafruit-circuitpython-motor`, `adafruit-blinka` |
| `lighting` | `adafruit_pixelbuf` and `rainbowio` | `adafruit-circuitpython-pixelbuf`, `adafruit-blinka` |
| `display` | `adafruit_display_shapes` and `displayio` | `adafruit-circuitpython-display-shapes`, `adafruit-blinka-displayio` |

`lighting.colors` does not require Adafruit modules.

## Deploying

### CircuitPython Devices

On CircuitPython devices, copy the required Adafruit libraries listed above to
the device's `lib` directory, along with their dependencies; `uv` does not
install packages on the device. `digitalio`, `displayio`, and `rainbowio` are
provided by CircuitPython on supported devices.

### Blinka Devices (and development)

Because the libraries are not published anywhere yet, you'll need to build the `.whl` yourself and then copy it to a "known location" and reference it specifically.

**EXample:**

> `uv add ../location/cp_crackers-0.1.0-py3-none-any.whl`

**NOTE:** you will (obviously) have to add/remove the package when the version changes.

If changing stuff around and re-building the library _without_ a version change, try:

> `uv lock --upgrade-package cp-crackers`
> `uv sync --reinstall-package cp-crackers`

to synchronize your target project.


## Stuff

TODO
