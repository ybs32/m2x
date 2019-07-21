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

if __name__ == '__main__':
    config = read_config(CONF_FILE_PATH)
    f = Ffmpeg(config['ffmpeg'])
    print(f.path)