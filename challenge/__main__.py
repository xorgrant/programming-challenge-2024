# Copyright 2023 (c) Xor Grant  https://github.com/xorgrant/programming-CHALLENGE-2024
#
# This source code is licensed under the MIT license.

from PIL import (
    Image,
    ImageDraw,
    ImageFont,
)

import base64
import constants
import functools
import math
import random
import textwrap


def RandomNoiseObfuscation(text: str) -> str:
    """Generate random character string and insert `text` to a specific position."""
    buffer: list[str] = [random.choice(constants.CHALLENGE_NOISE_CHARSET)
                         for _ in range(constants.CHALLENGE_NOISE_CHARSIZE)]
    buffer.insert(math.floor(len(buffer) * constants.CHALLENGE_NOISE_PARTITION), text)
    return "".join(buffer)


def Base64Obfuscation(text: str) -> str:
    """Encode `text` using base64."""
    return base64.b64encode(text.encode()).decode()


def TextWrapObfuscation(text: str, width: int = len(constants.CHALLENGE_HINT), *a, **kw) -> str:
    """Wrap a long `text` into multi-lines of `width` length."""
    wrap: list[str] = textwrap.wrap(text=text, width=width, *a, **kw)

    # Add a space between each characters to be rendered evenly-spaced.
    return "\n".join(" ".join(line) for line in wrap)


class Challenge(object):

    def __init__(self, puzzle: str, hint: str = ""):
        self.puzzle: str = puzzle
        self.hint: str = hint

        # Image (PIL) buffer.
        self._img: Image = None
        self._img_width: int = None
        self._img_height: int = None

    @property
    @functools.lru_cache(maxsize=1)
    def text(self) -> str:
        """Challenge raw text to be rendered."""
        return self.hint + constants.NEWLINE + self.puzzle

    def render(self, save_as: str, font: ImageFont.FreeTypeFont = ImageFont.load_default()) -> None:
        """Render challenge `text` into an image."""
        # Since it's challenging to manually find an image's optimal width/height dimension, identify
        # it by measuring the dimension of a rendered 'A' and scale it using `Challenge.text` string.
        (_, y0, _, y1) = font.getbbox('A')
        self._img_height: int = round(((y0 + y1) * (1 + self.text.count(constants.NEWLINE))))
        self._img_width: int = round(font.getlength('A') * (len(self.hint) + 1))

        self._img: Image = Image.new(
            mode="RGB",
            size=(self._img_width, self._img_height),
            color=constants.DISPLAY_BACKGROUND_COLOR,
        )

        painter: ImageDraw = ImageDraw.Draw(self._img)
        painter.multiline_text(
            xy=(0, 0),
            text=self.text,
            font=font,
            fill=constants.DISPLAY_FOREGROUND_COLOR,
            align="left",
        )

        # Minimize image compression for each characters to be as clear as possible.
        self._img.save(fp=save_as, quality=100, subsampling=0)


if __name__ == "__main__":
    Challenge(
        puzzle=TextWrapObfuscation(Base64Obfuscation(RandomNoiseObfuscation(constants.CHALLENGE_SOLUTION))),
        hint=TextWrapObfuscation(constants.CHALLENGE_HINT),
    ).render(save_as="programming_challenge_2024.bmp", font=constants.DISPLAY_FONT)
