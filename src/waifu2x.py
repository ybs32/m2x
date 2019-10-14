#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from module import Module


class Waifu2x(Module):

    def __init__(self, waifu2x_configs):
        super().__init__(waifu2x_configs)
        self.upscale_configs = waifu2x_configs['upscale']

    def upscale(self, input_dir, output_dir):
        args = [
            '-i',
            input_dir,
            '-o',
            output_dir
        ]
        args.extend(
            self._read_config(self.upscale_configs)
        )
        self._execute(args)
