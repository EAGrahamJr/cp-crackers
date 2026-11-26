import asyncio

from adafruit_pixelbuf import PixelBuf
from rainbowio import colorwheel

GAMMA8 = tuple(
    int((channel / 255) ** 2.8 * 255 + 0.5)
    for channel in range(256)
)


class NeoPixelEffects:
    def __init__(self):
        self.__carry_on = True

    def stop(self):
        self.__carry_on = False

    async def rainbow_cycle(
        self,
        strand: PixelBuf,
        pixels: range,
        wait: int | float,
        reverse: bool = False,
    ) -> None:
        """Cycle through the colors.

        Requires auto-update. Runs until stopped with the stop() method.

        Args:
            strand: The NeoPixel strand to animate.
            pixels: Nonempty, ascending range of valid, nonnegative strand indices.
            wait: The delay between color updates (in seconds).
            reverse: Whether to reverse the direction of the rainbow effect.
        """
        while self.__carry_on:
            for j in range(255):
                for offset, index in enumerate(pixels):
                    if not self.__carry_on:
                        return
                    rc_index = (offset * 256 // len(pixels)) + j
                    if reverse:
                        rc_index = 255 - rc_index
                    strand[index] = colorwheel(rc_index & 255)
                    await asyncio.sleep(wait)

    async def chase(
        self,
        strand: PixelBuf,
        pixels: range,
        color: tuple,
        wait: int | float = 0.05,
        dim_by: int = 20,
        reverse: bool = False,
    ) -> None:
        """Move a fading pixel along the strand until stopped.

        Requires auto-update. Runs until stopped with the stop() method.

        Args:
            strand: The NeoPixel strand to animate.
            pixels: Nonempty, ascending range of valid, nonnegative strand indices.
            color: The color of the chasing pixel.
            wait: The delay between updates (in seconds).
            dim_by: The amount to dim each pixel by on each update.
            reverse: Whether to reverse the direction of the chase.
        """
        pixel_slice = slice(pixels.start, pixels.stop, pixels.step)
        pos = 0
        while self.__carry_on:
            strand[pixels[pos]] = color
            strand[pixel_slice] = [
                (
                    max(strand[i][0] - dim_by, 0),
                    max(strand[i][1] - dim_by, 0),
                    max(strand[i][2] - dim_by, 0),
                )
                for i in pixels
            ]
            if reverse:
                pos = (pos - 1) % len(pixels)
            else:
                pos = (pos + 1) % len(pixels)
            await asyncio.sleep(wait)

