#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

from Source.Interfaz.InterfazEmpleado import InterfazEmpleado

class AplicationManager(wx.App):

    def __init__(self, redirect=True, filename=None, useBestVisual=False, clearSigInt=True):

        wx.App.__init__(self, redirect, filename, useBestVisual, clearSigInt)

    def OnInit(self):

        self.frame = InterfazEmpleado(parent=None, id=-1)
        self.SetTopWindow(self.frame)
        return True