#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelDatos(wx.Panel):


    def __init__(self, *args, **kw):

        super().__init__(*args, **kw)

        # Etiquetas del panel.
        self.etiquetaNombre = wx.StaticText(self, -1, 'Nombre:')

        self.etiquetaApellido = wx.StaticText(self, -1, 'Apellido:')

        self.etiquetaSexo = wx.StaticText(self, -1, 'Sexo:')

        self.etiquetaFechaN = wx.StaticText(self, -1, 'Fecha de Nacimiento:')

        self.etiquetaFechaI = wx.StaticText(self, -1, 'Fecha de Ingreso:')

        # Textos del panel.
        self.textoNombre = wx.StaticText(self, -1, '')

        self.textoApellido = wx.StaticText(self, -1, '')

        self.textoSexo = wx.StaticText(self, -1, '')

        self.textoFechaN = wx.StaticText(self, -1, '')

        self.textoFechaI = wx.StaticText(self, -1, '')

        # Le damos forma al panel.
        sizerLayout = wx.GridBagSizer()