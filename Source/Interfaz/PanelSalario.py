#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelSalario(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr, nNumeroCandidato=None):

        super().__init__(parent, id, pos, size, style, name)

        self.interfazEmpleado = parent

        self.etiquetaSalario = wx.StaticText(self, -1, 'Salario:')

        self.textoSalario = wx.StaticText(self, -1, '')

        self.botonCambiarSalario = wx.Button(self, -1, 'Modificar')


        sizerLayout = wx.BoxSizer(wx.HORIZONTAL)

        # Añadimos un componente vacio.
        sizerLayout.AddStretchSpacer(prop=1)
        sizerLayout.Add(self.etiquetaSalario, 0, wx.CENTRE)
        # Añadimos 5 pixeles de distancia entre componentes.
        sizerLayout.AddSpacer(5)
        sizerLayout.Add(self.textoSalario, 0, wx.CENTRE)
        # Añadimos 5 pixeles de distancia entre componentes.
        sizerLayout.AddSpacer(5)
        sizerLayout.Add(self.botonCambiarSalario, 0, wx.CENTRE)
        # Añadimos un componente vacio.
        sizerLayout.AddStretchSpacer(prop=1)

        self.SetSizer(sizerLayout)


    def ActualizarSalario(self, salario):

        self.textoSalario.SetLabel(str(salario))
        self.Layout()