#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import ctypes

try:
    # Reference: https://stackoverflow.com/a/54247018
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

from Source.App import AplicationManager

if __name__ == '__main__':
    app = AplicationManager()
    app.MainLoop()
