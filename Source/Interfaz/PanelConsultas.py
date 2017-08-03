#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelConsultas(wx.Panel):

    def __init__(self, *args, **kw):

        super().__init__(*args, **kw)

        self.botonEdad = wx.Button(self, -1, 'Calcular Edad')

        self.botonAntiguedad = wx.Button(self, -1, 'Calcular Antigüedad')

        self.botonPrestaciones = wx.Button(self, -1, 'Calcular Prestaciones')

        self.textoEdad = wx.StaticText(self, -1, 'Edad')

        self.textoAntiguedad = wx.StaticText(self, -1, 'Antigüedad')

        self.textoPrestaciones = wx.StaticText(self, -1, 'Prestaciones')

        # Le damos forma al panel.
        sizerLayoutVertical = wx.BoxSizer(wx.VERTICAL)
        sizerLayoutHorizontal = wx.BoxSizer(wx.HORIZONTAL)
        sizerLayout = wx.GridBagSizer(vgap=5, hgap=5)

        sizerLayout.Add(self.botonEdad, pos=(0, 0))
        sizerLayout.Add(self.botonAntiguedad, pos=(1, 0))
        sizerLayout.Add(self.botonPrestaciones, pos=(2, 0))
        sizerLayout.Add(self.textoEdad, pos=(0, 1))
        sizerLayout.Add(self.textoAntiguedad, pos=(1, 1))
        sizerLayout.Add(self.textoPrestaciones, pos=(2, 1))

        sizerLayoutVertical.Add(sizerLayoutHorizontal, 1, wx.ALIGN_CENTRE)
        sizerLayoutHorizontal.Add(sizerLayout, 1, wx.ALIGN_CENTRE)

        self.SetSizer(sizerLayoutVertical)


