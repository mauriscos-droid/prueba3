#============Espacios============
class espacio:
    def __init__(self, id_espacio,nombre,ubicacion):
        self.id_espacio = id_espacio
        self.nombre = nombre
        self.ubicacion = ubicacion

    def mostrar_detalles(self):
        print(f"El espacio es: {self.id_espacio}, {self.nombre} y se encuentra en {self.ubicacion}")

class salaCine(espacio):
    def __init__(self, id_espacio, nombre, ubicacion, tipo, capacidad):
        super().__init__(id_espacio, nombre, ubicacion)
        self.tipo = tipo
        self.capacidad = capacidad

    def mostrar_detalles(self):
        print(f"La sala es: {self.nombre}, de tipo {self.tipo} con capacidad de {self.capacidad} cupos")

class ZonaDeComida(espacio):
    def __init__(self,id_espacio, nombre, ubicacion):
        super().__init__(id_espacio, nombre, ubicacion)
        self.product_list = []
        self.stock = {}
    def mostrar_detalles(self):
        print(f"La zona de comida es: {self.nombre}, ubicada en {self.ubicacion}. Cuenta con los siguientes productos: {self.product_list}")
#============Personas============
class persona:
    def __init__(self, id_per, name, mail, phone):
        self.id= id_per
        self.name= name
        self.mail = mail
        self.phone = phone
    def mostrar_detalles(self):
        print(f"Nombre: {self.name}, Mail: {self.mail}, Numero de telefono: {self.phone}.")
class empleado(persona):
    def __init__(self, id_per, name, mail, phone, funcion, horario):
        super().__init__(id_per, name, mail, phone)
        self.id_empleado = id_per
        self.funcion= funcion
        self.horario= horario
    
    def mostrar_detalles(self):
        print(f"El empleado es: {self.name}, con mail: {self.mail} y su telefono es: {self.phone}. Su funcion es: {self.funcion} y su horario es: {self.horario}")

class usuario(persona):
    def __init__(self, id_per, name, mail, phone, puntos_fidelidad):
        super().__init__(id_per, name, mail, phone)
        self.puntos_fidelidad = puntos_fidelidad
        self.historial_reservas= []
    def mostrar_detalles(self):
        print(f"El usuario es: {self.name}, con mail: {self.mail} y su telefono es: {self.phone}. Tiene {self.puntos_fidelidad} puntos de fidelidad.")

#============Varios============
class pelicula:
    def __init__(self, id_pelicula, titulo, duracion, clasificacion, genero):
        self.id_pelicula = id_pelicula
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero
    def mostrar_detalles(self):
        print(f"La pelicula es: {self.titulo}, con duracion de: {self.duracion} minutos, con clasificacion: {self.clasificacion} y pertenece al genero de {self.genero}")

class funcion:
    def __init__(self, id_funcion, pelicula, horario, precio):
        self.id_funcion = id_funcion
        self.pelicula = pelicula
        self.horario = horario
        self.precio = precio
        self.asientos_ocupados = []

    def verificar_asientos(self, asientos):
        for asiento in asientos:
            if asiento in self.asientos_ocupados:
                return False, asiento
        return True, None

    def ocupar_asientos(self, asientos):
        self.asientos_ocupados.append(asientos)

    def mostrar_detalles(self):
        print(f"La funcion es: {self.id_funcion}, con la pelicula: {self.pelicula.titulo}, con horario de: {self.horario} y un precio de ${self.precio}")

class promo:
    def __init__(self,codigo, desc, percent_disc,total):
        self.codigo = codigo
        self.desc = desc
        self.percent_disc= percent_disc

class reserva:
    def __init__(self, id_reserva, usuario, funcion, asientos):
        self.id_reserva = id_reserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.total = 0.0
        self.estado="PENDIENTE"
    
    def calcular_total_base(self):
        self.total = len(self.asientos) * self.funcion.precio
        return self.total
    
    def aplicar_promocion(self, promocion):
        descuento = self.total * promocion.percent_disc
        self.total -= descuento
        return descuento
    
    def confirmar_reserva(self):
        self.estado = "PAGADA"

    def mostrar_estado(self):
        print(f"El estado de la promoción es: {self.estado}")
    
    def mostrar_detalles(self):
        print(f"La reserva es: {self.id_reserva}, del usuario {self.usuario.name}, para la funcion de {self.funcion.id_funcion} y en los asientos {self.asientos}. El total es de ${self.total} y el estado estado de su reserva es: {self.estado}")
        