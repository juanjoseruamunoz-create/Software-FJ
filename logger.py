# ===============================
# CONFIGURACIÓN DE LOGS
# ===============================

import logging

logging.basicConfig(
    filename='logs.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def registrar_log(mensaje):
    logging.info(mensaje)


def registrar_error(error):
    logging.error(error)