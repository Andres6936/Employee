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

    def __init__(self, d, m, a):
        """
        Inicializa una fecha con los parámetros proporcionados.

        Args:
            d (int): Día d > 0 y d <= 31 y d es un valor válido según el mes.
            m (int): Mes m > 0 y m <= 12.
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

    def InicializarHoy(self):
        """
        Construye una nueva fecha inicializada en el día de hoy.

        Poscondicion:

            El objecto fecha tiene sus datos básicos asignados con los datos del
            día de hoy.

        """

        calendarioGregoriano = datetime.date()

        self.dia = calendarioGregoriano.day
        self.mes = calendarioGregoriano.month
        self.anio = calendarioGregoriano.year

    def GetDia(self):

        return self.dia

    def GetMes(self):

        return self.mes

    def GetAnio(self):

        return self.anio

    def GetDiferenciaEnMeses(self, fecha):

        diferencia = 0

        otroAnio = fecha.GetAnio()
        otroMes = fecha.GetMes()
        otroDia = fecha.GetDia()

        # Calcula la diferencia en meses.
        diferencia = 12 * ( otroAnio - self.anio ) + ( otroMes - self.mes )

        # Si el día no es mayor, resta un mes
        if otroDia < self.dia:
            diferencia -= 1

        return diferencia

    def ToString(self):

        return "{0} {1} {2}".format(self.dia, self.mes, self.anio)