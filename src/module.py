#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess


class Module(object):

    def __init__(self, configs):
        self.path = configs['path']

    def _read_config(self, configs):
        args = []
        for key in configs.keys():
            args.append(key)
            args.append(str(configs[key]))
        return args

    def _execute(self, args):
        exec = [
            self.path
        ]
        exec.extend(args)
        subprocess.run(exec, shell=True)

    def _execute_ret(self, args):
        exec = [
            self.path
        ]
        exec.extend(args)
        proc = subprocess.run(exec, shell=True, stdout = subprocess.PIPE)
        return proc.stdout.decode("utf8")
