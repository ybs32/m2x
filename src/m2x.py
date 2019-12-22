#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import json
import shutil
from ffmpeg import Ffmpeg
from ffprobe import Ffprobe
from waifu2x import Waifu2x


CONF_FILE_PATH = '..\\config\\config.json'

def read_config(path):
    with open(path, 'r') as config:
        return json.load(config)

def mk_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def rm_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)

if __name__ == '__main__':
    config = read_config(CONF_FILE_PATH)

    dirs = config['dirs']
    ffmpeg = Ffmpeg(config['ffmpeg'])
    ffprobe = Ffprobe(config['ffprobe'])
    waifu2x = Waifu2x(config['waifu2x'])

    files = glob.glob(dirs['input'] + '\\*')
    for file in files:
        rm_dir(dirs['tmp'])
        for dir in dirs.values():
            mk_dir(dir)

        ffmpeg.extract_audio(file, dirs['audio'])
        ffmpeg.extract_images(file, dirs['img_in'])

        fps = ffprobe.read_fps(file)
        waifu2x.upscale(dirs['img_in'], dirs['img_out'])
        ffmpeg.compose(file, fps, dirs['img_out'], dirs['audio'], dirs['output'])
