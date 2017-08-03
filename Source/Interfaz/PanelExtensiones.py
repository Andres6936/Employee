#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelExtensiones(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):

        # Enviamos todos los parametros a la clase padre.
        super().__init__(parent, id, pos, size, style, name)

        self.principal = parent

        # Botón Opción 1.
        self.botonOpcion1 = wx.Button(self, -1, 'Opción 1')

        # Botón Opción 2.
        self.botonOpcion2 = wx.Button(self, -1, 'Opción 2')

        # Configuramos el Border Layout del panel.
        sizerLayout = wx.BoxSizer(wx.HORIZONTAL)

        sizerLayout.AddStretchSpacer(prop=1)
        sizerLayout.Add(self.botonOpcion1, 0)
        sizerLayout.Add(self.botonOpcion2, 0)
        sizerLayout.AddStretchSpacer(prop=1)

        self.SetSizer(sizerLayout)
        self.Fit()