# Copyright 2023 (c) Xor Grant  https://github.com/xorgrant/programming-CHALLENGE-2024
#
# This source code is licensed under the MIT license.

from challenge import *


if __name__ == "__main__":
    Challenge(
        puzzle=TextWrapObfuscation(Base64Obfuscation(RandomNoiseObfuscation(constants.CHALLENGE_SOLUTION))),
        hint=TextWrapObfuscation(constants.CHALLENGE_HINT),
    ).render(save_as="programming_challenge_2024.bmp", font=constants.DISPLAY_FONT)
