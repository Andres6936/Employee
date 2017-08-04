#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

from Source.Mundo.Empleado import Empleado

class PanelConsultas(wx.Panel):

    def __init__(self, *args, **kw):

        # Enviamos todos los parametros a la clase padre.
        super().__init__(*args, **kw)

        # Botón Calcular edad.
        self.botonEdad = wx.Button(self, -1, 'Calcular Edad')
        self.Bind(wx.EVT_BUTTON, self.OnCalcularEdad, self.botonEdad)

        # Botón Calcular antigüedad.
        self.botonAntiguedad = wx.Button(self, -1, 'Calcular Antigüedad')
        self.Bind(wx.EVT_BUTTON, self.OnCalcularAntiguedad, self.botonAntiguedad)

        # Botón Calcular prestaciones.
        self.botonPrestaciones = wx.Button(self, -1, 'Calcular Prestaciones')
        self.Bind(wx.EVT_BUTTON, self.OnCalcularPrestaciones, self.botonPrestaciones)

        # Texto edad.
        self.textoEdad = wx.StaticText(self, -1, 'Edad')

        # Texto antigüedad.
        self.textoAntiguedad = wx.StaticText(self, -1, 'Antigüedad')

        # Texto prestaciones.
        self.textoPrestaciones = wx.StaticText(self, -1, 'Prestaciones')

        # Atributo Empleado
        self.empleado: Empleado = None
        """
        El empleado sobre el que se realizan los cálculos.
        """

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


    def OnCalcularEdad(self, evento):

        edad = self.empleado.GetEdad()
        self.textoEdad.SetLabel(str(edad))

    def OnCalcularAntiguedad(self, evento):

        antiguedad = self.empleado.GetAntiguedad()
        self.textoAntiguedad.SetLabel(str(antiguedad))

    def OnCalcularPrestaciones(self, evento):

        prestaciones = self.empleado.GetPrestaciones()
        self.textoPrestaciones.SetLabel(str(prestaciones))

    def SetEmpleado(self, unEmpleado: Empleado) -> None:
        """
        Modifica el empleado que se utiliza para realizar los cálculos.

        Args:
            unEmpleado (Empleado): Nuevo empleado que se usará para los cálculos.
                *unEmpleado != None*.

        Poscondicion:
            empleado = unEmpleado.

        """

        self.empleado = unEmpleado

    def LimpiarCampos(self):
        """
        Limpia los campos.

        Poscondicion:
            Todos los campos del panel están limpios.

        """

        self.textoEdad.SetLabel('')
        self.textoAntiguedad.SetLabel('')
        self.textoPrestaciones.SetLabel('')