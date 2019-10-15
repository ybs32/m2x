#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
from module import Module


class Ffprobe(Module):

    def __init__(self, ffprobe_configs):
        super().__init__(ffprobe_configs)

    def test(self, file):
        args = [
            file
        ]
        self._execute(args)
