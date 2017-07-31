#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

from Source.Mundo.Fecha import Fecha

class Empleado(object):

    def __init__(self, nNombre, nApellido, nSexo, nFechaN, nFechaI, nSalario):

        self.nombre = nNombre
        self.apellido = nApellido
        self.sexo = nSexo
        self.fechaNacimiento = nFechaN
        self.fechaIngreso = nFechaI
        self.salario = nSalario
        self.imagen = None

    def GetNombre(self):

        return self.nombre

    def GetApellido(self):

        return self.apellido

    def GetSexo(self):

        return self.sexo

    def GetFechaNacimiento(self):

        return self.fechaNacimiento

    def GetFechaIngreso(self):

        return self.fechaIngreso

    def GetSalario(self):

        return self.salario

    def GetImagen(self):

        return self.imagen

    def GetEdad(self):

        hoy = Fecha(1, 1, 1)
        hoy.InicializarHoy()

        edad = self.fechaNacimiento.GetDiferenciaEnMeses( hoy ) / 12

        return edad

    def GetAntiguedad(self):

        hoy = Fecha(1, 1, 1)
        hoy.InicializarHoy()

        antiguedad = self.fechaIngreso.GetDiferenciaEnMeses( hoy ) / 12

        return antiguedad

    def GetPrestaciones(self):

        antiguedad = self.GetAntiguedad()

        prestaciones = float(( antiguedad * self.salario ) / 12)

        return prestaciones

    def SetFechaIngreso(self, nFechaIngreso):

        self.fechaIngreso = nFechaIngreso

    def SetImagen(self, nImagen):

        self.imagen = nImagen

    def SetSalario(self, nSalario):

        self.salario = nSalario

    def Metodo1(self):

        return "Respuesta 1"

    def Metodo2(self):

        return "Respuesta 2"