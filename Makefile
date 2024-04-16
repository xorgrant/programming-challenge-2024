# Copyright 2023 (c) Xor Grant  https://github.com/xorgrant/programming-challenge-2024
#
# This source code is licensed under the MIT license.

PROJECT   ?= $(shell pwd)
CHALLENGE ?= $(PROJECT)/challenge
SOLUTION  ?= $(PROJECT)/solution


.PHONY: all challenge solution

all: clean challenge solution

challenge:
	@python $(CHALLENGE)

solution:
	@python $(SOLUTION)

clean:
	@rm -rf $(PROJECT)/charset
	@rm -f  $(PROJECT)/programming_challenge_2024.bmp