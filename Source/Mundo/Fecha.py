#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

from datetime import datetime

class Fecha(object):
    """
    Esta clase sirve para representar una fecha y hacer algunas operaciones básicas.

    Attributes:

        dia (int): Día del mes.
        mes (int): Mes.
        anio (int): Año.

    """

    def __init__(self, d: int, m: int, a: int):
        """
        Inicializa una fecha con los parámetros proporcionados.

        Args:
            d (int): Día `d` > 0 y `d` <= 31 y `d` es un valor válido según el mes.
            m (int): Mes `m` > 0 y `m` <= 12.
            a (int): Año.

        Poscondicion:

            El objecto fecha tiene sus datos básicos asignado con los parámetros
            proporcionados.

        """

        self.dia = d
        """
        Día del mes.
        """

        self.mes = m
        """
        Més.
        """

        self.anio = a
        """
        Año.
        """

    def InicializarHoy(self) -> None:
        """
        Construye una nueva fecha inicializada en el día de hoy.

        Poscondicion:

            El objecto fecha tiene sus datos básicos asignados con los datos del
            día de hoy.

        """

        # Usamos un calendario Gregoriano inicializado en el día de hoy.
        calendarioGregoriano = datetime.now()

        # Sacamos lo valores del día, mes y año del calendario.
        self.dia = calendarioGregoriano.day
        self.mes = calendarioGregoriano.month
        self.anio = calendarioGregoriano.year

    def GetDia(self) -> int:
        """
        Retorna el día de esta fecha.

        Returns:

            int: día.

        """

        return self.dia

    def GetMes(self) -> int:
        """
        Retorna el mes de esta fecha.

        Returns:

            int: mes.

        """

        return self.mes

    def GetAnio(self) -> int:
        """
        Retorna el año de esta fecha.

        Returns:

            int: año.

        """

        return self.anio

    def GetDiferenciaEnMeses(self, fecha) -> int:
        """
        Este método sirve para dar la diferencia en meses que hay entre dos fechas.

        Args:
            fecha (Fecha): La fecha contra la que se está comparando. `fecha` != None.

        Returns:

            int: El número de meses.

        """

        otroAnio = fecha.GetAnio()
        otroMes = fecha.GetMes()
        otroDia = fecha.GetDia()

        # Calcula la diferencia en meses.
        diferencia = 12 * ( otroAnio - self.anio ) + ( otroMes - self.mes )

        # Si el día no es mayor, resta un mes
        if otroDia < self.dia:
            diferencia -= 1

        return diferencia

    def ToString(self) -> str:
        """
        Retorna una cadena que representa la fecha.

        Returns:

            str: La String sigue el formato día-mes-año.

        """

        return "{0} {1} {2}".format(self.dia, self.mes, self.anio)