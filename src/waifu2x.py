#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

class Waifu2x:

    def __init__(self, waifu2x_configs):
        self.waifu2x_configs = waifu2x_configs

    def convert(self, input_dir, output_dir):
        args = [
            '-i',
            input_dir,
            '-o',
            output_dir,
            '--model-dir',
            self.waifu2x_configs['--model-dir'],
            '--mode',
            str(self.waifu2x_configs['--mode']),
            '--noise-level',
            str(self.waifu2x_configs['--noise-level']),
            '--scale-ratio',
            str(self.waifu2x_configs['--scale-ratio'])
        ]
        self._execute(args)

    def _execute(self, args):
        exec = [
            self.waifu2x_configs['path']
        ]
        exec.extend(args)
        subprocess.run(exec, shell=True)
