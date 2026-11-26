# A Personal Circuit Python Library

This is just stuff I dorked up in various ways and don't want to repeat myself.

Use at your own risk.

## Dependencies

For desktop development, install the extras for the features you need:

```sh
uv sync --extra motor --extra lighting --extra display
```

Omit any extras you do not need, or use `uv sync --all-extras` to install all
of them. Select this project's `.venv` interpreter in VS Code. Blinka and the
hardware-dependent libraries require supported hardware to run.

## Deploying

### CircuitPython Devices

On CircuitPython devices, copy the required Adafruit libraries to the device's
`lib` directory; `uv` extras do not install packages on the device. Modules
such as `digitalio`, `displayio`, and `rainbowio` are provided by CircuitPython
on supported devices.

### Blinka Devices (and development)

Because the libraries are not published anywhere yet, you'll need to build the `.whl` yourself and then copy it to a "known location" and reference it specifically.

**EXample:**

> `uv add ../location/cp_crackers-0.1.0-py3-none-any.whl --extra display`

If changing stuff around and re-building the library, you should use something like:

> `uv lock --upgrade`
> `uv sync --reinstall-package cp-crackers`

## Stuff

TODO
