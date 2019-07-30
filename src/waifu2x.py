#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

class Waifu2x:

    def __init__(self, waifu2x_configs):
        self.path = waifu2x_configs['path']
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

    def _read_config(self, configs):
        args = []
        for key in configs.keys():
            args.append(key)
            args.append(str(configs[key]))
        return args

    def _execute(self, args):
        exec = [
            self.path
        ]
        exec.extend(args)
        subprocess.run(exec, shell=True)
