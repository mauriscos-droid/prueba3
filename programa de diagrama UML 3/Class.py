#CLASE MATERIAL
from datetime import datetime, timedelta
from typing import List
class Material():
    def __init__(self, IdMaterial, Titulo, Año_Publicacion, Disponibilidad):
        self.idMaterial = IdMaterial
        self.titulo = Titulo
        self.añoPublicacion = Año_Publicacion
        self.disponibilidad = Disponibilidad

    def __str__(self):
        estado = 'Disponible' if self.disponibilidad else 'Prestado'
        return f"[{self.idMaterial}] {self.titulo} ({self.añoPublicacion}) - {estado}"

class libro(Material):
    def __init__(self, IdMaterial, Titulo, Año_Publicacion, Disponibilidad, Autor, ISBN):
        super().__init__(IdMaterial, Titulo, Año_Publicacion, Disponibilidad)
        self.autor = Autor
        self.isbn = ISBN

class revista(Material):
    def __init__(self, IdMaterial, Titulo, Año_Publicacion, Disponibilidad, Edicion, Periodicidad):
        super().__init__(IdMaterial, Titulo, Año_Publicacion, Disponibilidad)
        self.edicion = Edicion
        self.periodicidad = Periodicidad

class Material_Digital(Material):
    def __init__(self, IdMaterial, Titulo, Año_Publicacion, Disponibilidad, Tipo_Archivo, Url_Descarga, Tamaño_MB):
        super().__init__(IdMaterial, Titulo, Año_Publicacion, Disponibilidad)
        self.tipoArchivo = Tipo_Archivo
        self.urlDescarga = Url_Descarga
        self.tamañoMB = Tamaño_MB

class prestamo():
    def __init__(self, IdPrestamo: int, Usuario, Material, Fecha_Prestamo: datetime, Fecha_Devolucion: datetime):
        self.idPrestamo = IdPrestamo
        self.usuario = Usuario
        self.material = Material
        self.fechaPrestamo = Fecha_Prestamo
        self.fechaDevolucion = Fecha_Devolucion

#CLASE PERSONA

class persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class usuario(persona):
    def __init__(self, Nombre, Apellido, Limite_Prestamos, Lista_Activa):
        super().__init__(Nombre, Apellido)
        self.limitePrestamos = Limite_Prestamos
        self.listaActiva = Lista_Activa if Lista_Activa is not None else []
    
    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido} Préstamos activos: {len(self.listaActiva)} Limite de prestamos:{self.limitePrestamos}"

class bibliotecario(persona):
    def __init__(self, nombre, apellido, idEmpleado):
        super().__init__(nombre, apellido)
        self.idEmpleado = idEmpleado

    def gestionarPrestamo(self, id_p, user, mat):
        if mat.disponibilidad and len(user.listaActiva) < user.limitePrestamos:
            fecha_actual = datetime.now()
            fecha_entrega = fecha_actual + timedelta(days=7)
            nuevo_p = prestamo(id_p, user, mat, fecha_actual, fecha_entrega)
            user.listaActiva.append(nuevo_p)
            mat.disponibilidad = False
            print(f"EXITO: {mat.titulo} prestado a {user.nombre}.")
            return nuevo_p
        else:
            print(f"ERROR: No se puede prestar {mat.titulo}.")

    def gestionarDevolucion(self, material, usuario):
        for prestamo in usuario.listaActiva:
            if prestamo.material.idMaterial == material.idMaterial:
                usuario.listaActiva.remove(prestamo)
                material.disponibilidad = True
                print(f"{material.titulo} ha sido devuelto por {usuario.nombre} {usuario.apellido}")
                return
        print(f"No se encontró un préstamo activo de {material.titulo} para {usuario.nombre} {usuario.apellido}")

class penalizacion():
    def __init__(self, monto, motivo):
        self.monto = monto
        self.motivo = motivo

    def calcularPenalizacion(self, diasRetraso):
        multa = 0.5
        self.monto = diasRetraso * multa
        print(f"Multa calculada: ${self.monto} por {diasRetraso} días de retraso. Motivo: {self.motivo}")

    def bloquearUsuario(self, usuario):
        if self.monto > 0:
            usuario.limitePrestamos = 0
            print(f"Usuario {usuario.nombre} {usuario.apellido} ha sido bloqueado debido a una penalización de ${self.monto}.")