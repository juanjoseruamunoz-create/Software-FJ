# ===============================
# CLASE RESERVA
# ===============================

from excepciones import ReservaError
from logger import registrar_log


class Reserva:

    def __init__(self, cliente, servicio, horas):

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    # Confirmar reserva
    def confirmar(self):

        if self.horas <= 0:
            raise ReservaError("La duración debe ser mayor que cero")

        self.estado = "Confirmada"

        registrar_log(
            f"Reserva confirmada para {self.cliente.get_nombre()}"
        )

    # Cancelar reserva
    def cancelar(self):

        self.estado = "Cancelada"

        registrar_log(
            f"Reserva cancelada para {self.cliente.get_nombre()}"
        )

    # Procesar reserva
    def procesar(self):

        costo = self.servicio.calcular_costo(self.horas)

        return f"Reserva procesada | Cliente: {self.cliente.get_nombre()} | Costo: ${costo}"