#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

from Source.Interfaz.PanelExtensiones import PanelExtensiones
from Source.Interfaz.PanelConsultas import PanelConsultas
from Source.Interfaz.PanelSalario import PanelSalario
from Source.Interfaz.PanelDatos import PanelDatos

class InterfazEmpleado(wx.Frame):

    def __init__(self, *args, **kw):

        super().__init__(*args, **kw)

        self.SetBackgroundColour('White')

        self.SetTitle('Sistema de Empleados')
        self.SetSize(wx.Size(530, 530))
        self.SetMaxSize(wx.Size(530, 530))
        self.SetMinSize(wx.Size(530, 530))
        self.Show(True)

        # Construye los paneles.
        self.panelDatos = PanelDatos(self, -1)
        self.panelSalario = PanelSalario(self, -1)
        self.panelConsultas = PanelConsultas(self, -1)
        self.panelExtensiones = PanelExtensiones(self, -1)

        # Construye la forma del Frame.
        sizerLayout = wx.BoxSizer(wx.VERTICAL)

        sizerLayoutDatos = wx.StaticBoxSizer(wx.VERTICAL, self, 'Datos Personales')
        sizerLayoutSalario = wx.StaticBoxSizer(wx.VERTICAL, self, 'Salario')
        sizerLayoutCalculos = wx.StaticBoxSizer(wx.VERTICAL, self, 'Cálculos')
        sizerLayoutExtension = wx.StaticBoxSizer(wx.VERTICAL, self, 'Puntos de Extensión')

        sizerLayoutDatos.Add(self.panelDatos, 1, wx.EXPAND)
        sizerLayoutSalario.Add(self.panelSalario, 1, wx.EXPAND)
        sizerLayoutCalculos.Add(self.panelConsultas, 1, wx.EXPAND)
        sizerLayoutExtension.Add(self.panelExtensiones, 1, wx.EXPAND)

        sizerLayout.Add(sizerLayoutDatos, 1, wx.EXPAND)
        sizerLayout.Add(sizerLayoutSalario, 1, wx.EXPAND)
        sizerLayout.Add(sizerLayoutCalculos, 1, wx.EXPAND)
        sizerLayout.Add(sizerLayoutExtension, 1, wx.EXPAND)

        self.SetSizer(sizerLayout)
        self.Layout()
        self.Fit()


    def ActualizarEmpleado(self):
        pass

    def ModificarSalario(self):
        pass

    def ReqFuncOpcion1(self):
        pass

    def ReqFuncOpcion2(self):
        pass