from clientes import Cliente
from servicios import ReservaSala
from servicios import AlquilerEquipo
from servicios import AsesoriaEspecializada
from reservas import Reserva
from logger import registrar_error


print("SISTEMA SOFTWARE FJ")
print("-" * 40)

# ===============================
# LISTAS DEL SISTEMA
# ===============================

clientes = []
reservas = []

# ===============================
# OPERACIÓN 1
# CLIENTE VÁLIDO
# ===============================

try:

    cliente1 = Cliente("Juan", "juan@gmail.com", 20)

    clientes.append(cliente1)

    print(cliente1.mostrar_info())

except Exception as e:

    registrar_error(e)


# ===============================
# OPERACIÓN 2
# CLIENTE INVÁLIDO
# ===============================

try:

    cliente2 = Cliente("", "correo_malo", -5)

    clientes.append(cliente2)

except Exception as e:

    print("Error al registrar cliente")

    registrar_error(e)


# ===============================
# OPERACIÓN 3
# CREACIÓN DE SERVICIOS
# ===============================

try:

    sala = ReservaSala("Sala VIP", 50)

    print(sala.descripcion())

except Exception as e:

    registrar_error(e)


# ===============================
# OPERACIÓN 4
# ALQUILER DE EQUIPOS
# ===============================

try:

    equipo = AlquilerEquipo("Computadores", 30)

    print(equipo.descripcion())

except Exception as e:

    registrar_error(e)


# ===============================
# OPERACIÓN 5
# ASESORÍA ESPECIALIZADA
# ===============================

try:

    asesoria = AsesoriaEspecializada("Asesoría TI", 100)

    print(asesoria.descripcion())

except Exception as e:

    registrar_error(e)


# ===============================
# OPERACIÓN 6
# RESERVA EXITOSA
# ===============================

try:

    reserva1 = Reserva(cliente1, sala, 2)

    reserva1.confirmar()

    print(reserva1.procesar())

    reservas.append(reserva1)

except Exception as e:

    print("Error en reserva")

    registrar_error(e)


# ===============================
# OPERACIÓN 7
# RESERVA FALLIDA
# ===============================

try:

    reserva2 = Reserva(cliente1, sala, -2)

    reserva2.confirmar()

    reservas.append(reserva2)

except Exception as e:

    print("Reserva inválida")

    registrar_error(e)


# ===============================
# OPERACIÓN 8
# ALQUILER CORRECTO
# ===============================

try:

    reserva3 = Reserva(cliente1, equipo, 3)

    reserva3.confirmar()

    print(reserva3.procesar())

    reservas.append(reserva3)

except Exception as e:

    registrar_error(e)


# ===============================
# OPERACIÓN 9
# ASESORÍA CORRECTA
# ===============================

try:

    reserva4 = Reserva(cliente1, asesoria, 1)

    reserva4.confirmar()

    print(reserva4.procesar())

    reservas.append(reserva4)

except Exception as e:

    registrar_error(e)


# ===============================
# OPERACIÓN 10
# CANCELACIÓN
# ===============================

try:

    reserva4.cancelar()

    print("Reserva cancelada correctamente")

except Exception as e:

    registrar_error(e)


print("-" * 40)
print("El sistema continúa funcionando correctamente")