#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import subprocess

class Ffmpeg:

    def __init__(self, ffmpeg_configs):
        self.path = ffmpeg_configs['path']
        self.mtoi_configs = ffmpeg_configs['movie_to_images']
        self.itom_configs = ffmpeg_configs['images_to_movie']

    def extract_audio(self, file, output_dir):
        args = [
            '-i',
            file,
            '-vn',
            os.path.join(output_dir, os.path.basename(file) + '.wav')
        ]
        self._execute(args)

    def extract_images(self, file, output_dir):
        args = [
            '-i',
            file
        ]
        args.extend(
            self._read_config(self.mtoi_configs)
        )
        args.append(
            os.path.join(output_dir, 'img_%07d.jpg')
        )
        self._execute(args)

    def compose(self, file, image_dir, audio_dir, output_dir):
        self._rename_images(image_dir)

        args = [
            '-i',
            os.path.join(image_dir, 'img_%07d.png'),
            '-i',
            os.path.join(audio_dir, os.path.basename(file) + '.wav')
        ]
        args.extend(
            self._read_config(self.itom_configs)
        )
        args.append(
            os.path.join(output_dir, os.path.basename(file) + '_converted.mp4')
        )
        self._execute(args)

    def _read_config(self, configs):
        args = []
        for key in configs.keys():
            args.append(key)
            args.append(str(configs[key]))
        return args

    def _rename_images(self, image_dir):
        files = glob.glob(image_dir + '\\*')
        for i, file in enumerate(files, 1):
            os.rename(file, os.path.join(image_dir, 'img_' + "{0:07d}".format(i) + '.png'))

    def _execute(self, args):
        exec = [
            self.path
        ]
        exec.extend(args)
        subprocess.run(exec, shell=True)
