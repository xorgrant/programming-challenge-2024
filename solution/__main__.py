# Copyright 2023 (c) Xor Grant  https://github.com/xorgrant/programming-challenge-2024
#
# This source code is licensed under the MIT license.

from split_image import split_image

import base64
import hashlib
import os
import re
import string

TemplateCharset: str = 'base64=' + string.ascii_uppercase + string.ascii_lowercase + string.digits


if __name__ == "__main__":
    # The purpose of this challenge is to employ automated parsing to decode the characters
    # using Base64. The challenge string's length has intentionally been set to deter manual
    # transcription, prompting reliance on image recognition techniques instead.
    #
    # This approach offers an alternative method, which I find somewhat simpler than employing
    # image recognition. By conceptualizing the problem as a grid of characters with fixed
    # positions, all represented in the same font, we can efficiently chart out all the
    # characters by conducting a one-time mapping of the template characters in the initial row.
    split_image(
        "programming_challenge_2024.bmp",
        195,
        len(TemplateCharset),
        output_dir="charset/",
        should_cleanup=False,
        should_quiet=True,
        should_square=False,
    )

    # Sort the files by the natural order (1..10).
    files: list[str] = sorted(sorted(os.listdir("charset/")), key=len)

    # Generate a hash map of the template characters.
    charset: dict[str, str] = {
        hashlib.md5(open(f"charset/{files[i]}", "rb").read()).hexdigest(): TemplateCharset[i]
        for i in range(len(TemplateCharset))
    }

    # Match each character block against the character map.
    text: str = "".join([
        charset.get(hashlib.md5(open(f"charset/{f}", "rb").read()).hexdigest(), "")
        for f in files
    ])

    # Decode the characters using Base64.
    text_decoded: str = base64.b64decode(text[len(TemplateCharset):]).decode()

    # Identify the flag based on `___flag{}___` pattern.
    print(re.findall(r'___flag{.*}___', text_decoded))
