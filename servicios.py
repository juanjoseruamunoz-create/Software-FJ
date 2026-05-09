# ===============================
# CLASE ABSTRACTA SERVICIO
# ===============================

from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponibleError


class Servicio(ABC):

    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    # Método abstracto
    @abstractmethod
    def calcular_costo(self, horas):
        pass

    # Método abstracto
    @abstractmethod
    def descripcion(self):
        pass


# ===============================
# SERVICIO RESERVA DE SALA
# ===============================

class ReservaSala(Servicio):

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ServicioNoDisponibleError("Horas inválidas para reserva")

        return self.precio_base * horas

    def descripcion(self):
        return "Servicio de reserva de salas"


# ===============================
# SERVICIO ALQUILER DE EQUIPOS
# ===============================

class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ServicioNoDisponibleError("Horas inválidas para alquiler")

        return (self.precio_base * horas) + 20

    def descripcion(self):
        return "Servicio de alquiler de equipos"


# ===============================
# SERVICIO DE ASESORÍA
# ===============================

class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ServicioNoDisponibleError("Horas inválidas para asesoría")

        return (self.precio_base * horas) * 1.15

    def descripcion(self):
        return "Servicio de asesoría especializada"