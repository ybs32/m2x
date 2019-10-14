#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import json
import shutil
from ffmpeg import Ffmpeg
from waifu2x import Waifu2x


CONF_FILE_PATH = '..\\config.json'

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
    f = Ffmpeg(config['ffmpeg'])
    w = Waifu2x(config['waifu2x'])

    files = glob.glob(dirs['input'] + '\\*')
    for file in files:
        rm_dir(dirs['tmp'])
        for dir in dirs.values():
            mk_dir(dir)

        f.extract_audio(file, dirs['audio'])
        f.extract_images(file, dirs['img_in'])

        w.upscale(dirs['img_in'], dirs['img_out'])
        f.compose(file, dirs['img_out'], dirs['audio'], dirs['output'])
