from excepciones import ClienteInvalidoError


class Cliente:

    def __init__(self, nombre, correo, edad):

        self.__nombre = nombre
        self.__correo = correo
        self.__edad = edad

        self.validar_datos()

    def validar_datos(self):

        if self.__nombre.strip() == "":
            raise ClienteInvalidoError("El nombre no puede estar vacío")

        if "@" not in self.__correo:
            raise ClienteInvalidoError("Correo inválido")

        if self.__edad <= 0:
            raise ClienteInvalidoError("La edad debe ser mayor que cero")

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_edad(self):
        return self.__edad

    def mostrar_info(self):

        return f"Cliente: {self.__nombre} | Correo: {self.__correo} | Edad: {self.__edad}"