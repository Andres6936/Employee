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
from Source.Mundo.Empleado import Empleado

class InterfazEmpleado(wx.Frame):

    def __init__(self, empleado, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name=wx.FrameNameStr):

        super().__init__(parent, id, title, pos, size, style, name)

        self.SetBackgroundColour('White')

        self.SetTitle('Sistema de Empleados')
        self.SetSize(wx.Size(530, 530))
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
        sizerLayout.Add(sizerLayoutSalario, 0, wx.EXPAND)
        sizerLayout.Add(sizerLayoutCalculos, 1, wx.EXPAND)
        sizerLayout.Add(sizerLayoutExtension, 0, wx.EXPAND)

        # Atributo Empleado
        self.empleado: Empleado = empleado
        self.panelConsultas.SetEmpleado(self.empleado)

        self.SetSizer(sizerLayout)
        self.Layout()
        self.Fit()


    def ActualizarEmpleado(self):

        # Variables locales
        nombre: str = self.empleado.GetNombre()
        apellido: str = self.empleado.GetApellido()

        iSexo: int = self.empleado.GetSexo()

        if iSexo == 1:
            sexo = 'M'
        else:
            sexo = 'F'

        fechaI: str = self.empleado.GetFechaIngreso()
        fechaN: str = self.empleado.GetFechaNacimiento()
        salario: int = self.empleado.GetSalario()
        imagen: str = self.empleado.GetImagen()

        self.panelDatos.ActualizarCampos(nombre, apellido, sexo, fechaI, fechaN, imagen)
        self.panelSalario.ActualizarSalario(salario)

        self.panelConsultas.LimpiarCampos()


    def ModificarSalario(self):
        pass

    def ReqFuncOpcion1(self):

        resultado = self.empleado.Metodo1()
        wx.MessageBox(resultado, 'Respuesta', wx.OK | wx.ICON_INFORMATION)

    def ReqFuncOpcion2(self):

        resultado = self.empleado.Metodo2()
        wx.MessageBox(resultado, 'Respuesta', wx.OK | wx.ICON_INFORMATION)