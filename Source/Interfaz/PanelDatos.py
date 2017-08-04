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
        self.textoNombre.SetLabel('Paola')

        self.textoApellido = wx.StaticText(self, -1, '')
        self.textoApellido.SetLabel('Villamil')

        self.textoSexo = wx.StaticText(self, -1, '')
        self.textoSexo.SetLabel('F')

        self.textoFechaN = wx.StaticText(self, -1, '')
        self.textoFechaN.SetLabel('14/25/1998')

        self.textoFechaI = wx.StaticText(self, -1, '')
        self.textoFechaI.SetLabel('25/54/1558')

        # Le damos forma al panel.
        sizerLayoutMain = wx.BoxSizer(wx.VERTICAL)
        self.sizerLayout = wx.GridBagSizer(vgap=20, hgap=20)

        # Imagen del empleado.
        self.imagen = wx.StaticBitmap(self, -1)

        self.sizerLayout.Add(self.etiquetaNombre, pos=(0, 0))
        self.sizerLayout.Add(self.etiquetaApellido, pos=(1, 0))
        self.sizerLayout.Add(self.etiquetaSexo, pos=(2, 0))
        self.sizerLayout.Add(self.etiquetaFechaN, pos=(3, 0))
        self.sizerLayout.Add(self.etiquetaFechaI, pos=(4, 0))
        self.sizerLayout.Add(self.textoNombre, pos=(0, 1))
        self.sizerLayout.Add(self.textoApellido, pos=(1, 1))
        self.sizerLayout.Add(self.textoSexo, pos=(2, 1))
        self.sizerLayout.Add(self.textoFechaN, pos=(3, 1))
        self.sizerLayout.Add(self.textoFechaI, pos=(4, 1))
        self.sizerLayout.Add(self.imagen, pos=(0, 2), span=(5, 1))

        sizerLayoutMain.Add(self.sizerLayout, 0, wx.ALIGN_CENTER)

        self.SetSizer(sizerLayoutMain)


    def ActualizarCampos(self, nombre, apellido, sexo, fechaI, fechaN, imagen):

        self.textoNombre.SetLabel(nombre)
        self.textoApellido.SetLabel(apellido)
        self.textoSexo.SetLabel(sexo)
        self.textoFechaI.SetLabel(fechaI)
        self.textoFechaN.SetLabel(fechaN)

        # Establecemos la imagen en el StaticBitmap.
        self.imagen.SetBitmap(self.CargarImagen(imagen))
        # Llamada al método Layout para acomodar el panel.
        self.Layout()

    def CargarImagen(self, imagen) -> wx.Bitmap:

        rutaImagen = imagen
        bitmap = wx.Bitmap(rutaImagen, wx.BITMAP_TYPE_JPEG)

        return bitmap