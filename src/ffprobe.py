#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from module import Module


class Ffprobe(Module):

    def __init__(self, ffprobe_configs):
        super().__init__(ffprobe_configs)

    def read_fps(self, file):
        args = [
            "-show_streams",
            "-of",
            "json",
            file
        ]
        info = self._executeExt(args)
        info_json = json.loads(info)
        frame_rate = info_json['streams'][0]['avg_frame_rate'].split('/')[0]
        return frame_rate
