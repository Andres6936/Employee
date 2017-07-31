#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

from Source.Mundo.Fecha import Fecha

class Empleado(object):
    """
    Esta clase representa un empleado.
    """

    def __init__(self, nNombre, nApellido, nSexo, nFechaN, nFechaI, nSalario):
        """
        Inicializa un empleado con la información básica.

        Poscondicion:

            El objecto empleado tiene sus datos básicos asignados.

        Args:

            nNombre (str): El nombre del empleado. `nNombre` != None.
            nApellido (str): El apellido del empleado. `nApellido` != None.
            nSexo (int): El sexo del empleado. `nSexo` pertenece a {1, 2}.
            nFechaN (Fecha): La fecha de nacimiento del empleado. `nFechaN` != None.
            nFechaI (Fecha): La fecha de ingreso del empleado. `nFechaI` != None.
            nSalario (int): El salario del empleado. `nSalario` != None.

        """

        self.nombre = nNombre
        """
        Nombre.
        """

        self.apellido = nApellido
        """
        Apellido.
        """

        self.sexo = nSexo
        """
        Sexo o género.
        """

        self.fechaNacimiento = nFechaN
        """
        Fecha de nacimiento.
        """

        self.fechaIngreso = nFechaI
        """
        Fecha de ingreso.
        """

        self.salario = nSalario
        """
        Salario.
        """

        self.imagen = None
        """
        Ruta de la imagen.
        """

    def GetNombre(self) -> str:
        """
        Retorna el nombre del empleado.

        Returns:

            str: nombre.

        """

        return self.nombre

    def GetApellido(self) -> str:
        """
        Retorna el apellido del empleado.

        Returns:

            str: apellido.

        """

        return self.apellido

    def GetSexo(self) -> int:
        """
        Retorna el sexo del empleado.

        Returns:

            int: sexo. *sexo* pertenece a {1, 2}.

        """

        return self.sexo

    def GetFechaNacimiento(self) -> str:
        """
        Retorna la fecha de nacimiento del empleado en una String.

        Returns:

            str: fechaNacimiento.

        """

        strFecha = self.fechaNacimiento.ToString()

        return strFecha

    def GetFechaIngreso(self) -> str:
        """
        Retorna la fecha de ingreso del empleado en una String.

        Returns:

            str: fechaIngreso.

        """

        strFecha = self.fechaIngreso.ToString()

        return strFecha

    def GetSalario(self) -> int:
        """
        Retorna el salario del empleado.

        Returns:

            int: salario.

        """

        return self.salario

    def GetImagen(self) -> str:
        """
        Retorna la ruta donde se encuentra la imagen del empleado.

        Returns:

            str: imagen.

        """

        return self.imagen

    def GetEdad(self) -> int:
        """
        Retorna la edad de la persona en años.

        Returns:

            int: Edad de la persona.

        """

        hoy = Fecha(1, 1, 1)
        hoy.InicializarHoy()

        edad = int(self.fechaNacimiento.GetDiferenciaEnMeses( hoy ) / 12)

        return edad

    def GetAntiguedad(self) -> int:
        """
        Retorna la antigüedad del empleado en años.

        Returns:

            int: Antigüedad del empleado.

        """

        hoy = Fecha(1, 1, 1)
        hoy.InicializarHoy()

        antiguedad = int(self.fechaIngreso.GetDiferenciaEnMeses( hoy ) / 12)

        return antiguedad

    def GetPrestaciones(self) -> float:
        """
        Este método sirve para saber las prestaciones del empleado usando la
        fórmula: p = (a * s) / 12 donde (p: prestaciones, a: antigüedad,
        s: salario).

        Notes:
            La antigüedad que se utiliza está dada en años, así que si un empleado
            lleva menos de un año en la empresa, sus prestaciones serán 0.

        Returns:

            float: Prestaciones a las que tiene derecho.

        """

        antiguedad = self.GetAntiguedad()

        prestaciones = float(( antiguedad * self.salario ) / 12)

        return prestaciones

    def SetFechaIngreso(self, nFechaIngreso: Fecha) -> None:
        """
        Cambia la fecha de ingreso del empleado.

        Args:
            nFechaIngreso (Fecha): La nueva fecha de ingreso del empleado.
                *nFechaIngreso* != None.

        Poscondicion:

            fechaIngreso == nFechaIngreso.

        """

        self.fechaIngreso = nFechaIngreso

    def SetImagen(self, nImagen: Fecha) -> None:
        """
        Cambia la ruta donde está la imagen del empleado.

        Args:
            nImagen (str): La nueva ruta de la imagen del empleado. *nImagen* != None.

        Poscondicion:

            imagen == nImagen.

        """

        self.imagen = nImagen

    def SetSalario(self, nSalario: int) -> None:
        """
        Cambia el salario del empleado.

        Args:
            nSalario (int): El nuevo salario del empleado.

        Poscondicion:

            salario == nSalario.

        """

        self.salario = nSalario

    def Metodo1(self):
        """
        Método de extensión 1.

        Returns:

            Resultado de la operación.

        """

        return "Respuesta 1"

    def Metodo2(self):
        """
        Método de extensión 2.

        Returns:

            Resultado de la operación.

        """

        return "Respuesta 2"