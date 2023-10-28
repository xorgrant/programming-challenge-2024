# Copyright 2023 (c) Xor Grant  https://github.com/xorgrant/programming-CHALLENGE-2024
#
# This source code is licensed under the MIT license.

PROJECT ?= $(shell pwd)
SOURCE  ?= $(PROJECT)/challenge

all: clean build

build:
	python $(SOURCE)

clean:
	@find $(PROJECT) -type d -name "__pycache__" -exec rm -rf "{}" \; || true
	@find $(PROJECT) -type f -iname "*.bmp" -exec rm -f "{}" \;
