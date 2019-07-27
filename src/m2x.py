#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import shutil
import subprocess
from ffmpeg import Ffmpeg

CONF_FILE_PATH = '.\\config.json'

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

    rm_dir(dirs['tmp'])
    for dir in dirs.values():
        mk_dir(dir)

    f = Ffmpeg(config['ffmpeg'])
    f.movie_to_audio(dirs['input'], dirs['audio'])
