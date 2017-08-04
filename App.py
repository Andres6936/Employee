#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

from Source.Interfaz.InterfazEmpleado import InterfazEmpleado
from Source.Mundo.Empleado import Empleado
from Source.Mundo.Fecha import Fecha

class AplicationManager(wx.App):

    def __init__(self, redirect=True, filename=None, useBestVisual=False, clearSigInt=True):

        wx.App.__init__(self, redirect, filename, useBestVisual, clearSigInt)

    def OnInit(self):

        # Creacón del empleado.
        fechaNacimiento = Fecha(16, 6, 1982)
        fechaIngreso = Fecha(5, 4, 2000)

        empleado = Empleado('Pedro', 'Matallana', 1, fechaNacimiento, fechaIngreso, 1500000)
        empleado.SetImagen('./Data/Empleado.jpg')

        self.frame = InterfazEmpleado(empleado=empleado, parent=None, id=-1)
        self.SetTopWindow(self.frame)
        self.frame.ActualizarEmpleado()
        return True