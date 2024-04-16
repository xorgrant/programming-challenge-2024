# Copyright 2023 (c) Xor Grant  https://github.com/xorgrant/programming-challenge-2024
#
# This source code is licensed under the MIT license.

from PIL import ImageFont

import string


NEWLINE: str = "\n"

(
    CHALLENGE_SOLUTION := "___flag{h0uston_w3_have_a_pr0blem}___",
    CHALLENGE_HINT     := "base64=" + string.ascii_uppercase + string.ascii_lowercase + string.digits,

    CHALLENGE_NOISE_MAXSIZE   := 10_000,  # characters
    CHALLENGE_NOISE_CHARSIZE  := CHALLENGE_NOISE_MAXSIZE - len(CHALLENGE_SOLUTION),  # characters
    CHALLENGE_NOISE_CHARSET   := "AaO0o",
    CHALLENGE_NOISE_PARTITION := 0.75,

    DISPLAY_FONT_FAMILY := "challenge/fonts/Terminus.ttf",
    DISPLAY_FONT_SIZE   := 17,
    DISPLAY_FONT        := ImageFont.truetype(
        font=DISPLAY_FONT_FAMILY,
        size=DISPLAY_FONT_SIZE,
    ),

    DISPLAY_BACKGROUND_COLOR := "white",
    DISPLAY_FOREGROUND_COLOR := "black",
)
