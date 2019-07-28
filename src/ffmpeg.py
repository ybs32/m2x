#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import subprocess

class Ffmpeg:

    def __init__(self, ffmpeg_configs):
        self.ffmpeg_configs = ffmpeg_configs
        self.mtoi_configs = ffmpeg_configs['movie_to_images']
        self.itom_configs = ffmpeg_configs['images_to_movie']

    def extract_audio(self, file, output_dir):
        args = [
            '-i',
            file,
            '-vn',
            os.path.join(output_dir, os.path.basename(file) + '.wav'),
        ]
        self._execute(args)

    def extract_images(self, file, output_dir):
        args = [
            '-i',
            file,
            '-f',
            self.mtoi_configs['-f'],
            '-vcodec',
            self.mtoi_configs['-vcodec'],
            '-qscale',
            str(self.mtoi_configs['-qscale']),
            '-qmin',
            str(self.mtoi_configs['-qmin']),
            '-qmax',
            str(self.mtoi_configs['-qmax']),
            os.path.join(output_dir, 'img_%07d.jpg')
        ]
        self._execute(args)

    def compose(self, file, image_dir, audio_dir, output_dir):
        self._rename_images(image_dir)

        args = [
            '-i',
            os.path.join(image_dir, 'img_%07d.png'),
            '-i',
            os.path.join(audio_dir, os.path.basename(file) + '.wav'),
            '-f',
            self.itom_configs['-f'],
            '-vcodec',
            self.itom_configs['-vcodec'],
            '-bufsize',
            self.itom_configs['-bufsize'],
            '-maxrate',
            self.itom_configs['-maxrate'],
            '-pix_fmt',
            self.itom_configs['-pix_fmt'],
            os.path.join(output_dir, os.path.basename(file) + '_converted.mp4')
        ]
        self._execute(args)

    def _rename_images(self, image_dir):
        files = glob.glob(image_dir + '\\*')
        for i, file in enumerate(files, 1):
            os.rename(file, os.path.join(image_dir, 'img_' + "{0:07d}".format(i) + '.png'))

    def _execute(self, args):
        exec = [
            self.ffmpeg_configs['path']
        ]
        exec.extend(args)
        subprocess.run(exec, shell=True)
