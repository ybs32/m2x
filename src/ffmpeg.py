#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

class Ffmpeg:

    def __init__(self, ffmpeg_configs):
        self.path = ffmpeg_configs['path']

    def movie_to_audio(self, input_dir, output_dir):
        files = os.listdir(input_dir)

        for file in files:
            args = [
                '-i',
                os.path.join(input_dir, file),
                '-vn',
                os.path.join(output_dir, file + '.wav'),
            ]
            self._execute(args)

    def _execute(self, args):
        exec = [
            self.path
        ]
        exec.extend(args)
        subprocess.run(exec, shell=True)
