# main.py
from datetime import datetime
# Asumiendo que guardaste tus clases en un archivo llamado models.py
from Class import libro, revista, Material_Digital, usuario, bibliotecario, prestamo, penalizacion

libros = []
libros.append(libro("001", "El Código de Python", 2020, True, "Juan Pérez", "ISBN-001"))
libros.append(libro("002", "Data Science con Python", 2021, False, "María García", "ISBN-002"))
libros.append(libro("003", "Machine Learning Avanzado", 2022, True, "Carlos López", "ISBN-003"))
libros.append(libro("004", "Python para Principiantes", 2019, False, "Ana Martínez", "ISBN-004"))
libros.append(libro("005", "Automatización con Python", 2023, True, "Luis Fernández", "ISBN-005"))
libros.append(libro("006", "Python en la Nube", 2020, True, "Sofía Gómez", "ISBN-006"))
libros.append(libro("007", "Desarrollo Web con Python", 2021, False, "Miguel Sánchez", "ISBN-007"))
libros.append(libro("008", "Python para Ciencia de Datos", 2022, True, "Laura Rodríguez", "ISBN-008"))
libros.append(libro("009", "Inteligencia Artificial con Python", 2023, True, "Javier Torres", "ISBN-009"))
libros.append(libro("010", "Python para Análisis de Datos", 2019, False, "Elena Díaz", "ISBN-010"))

revistas = []
revistas.append(revista("001", "Revista de Tecnología", 2021, True, "Vol. 10", "Mensual"))
revistas.append(revista("002", "Revista de Ciencia", 2020, False, "Vol. 5", "Trimestral"))
revistas.append(revista("003", "Revista de Programación", 2022, True, "Vol. 3", "Semestral"))
revistas.append(revista("004", "Revista de Innovación", 2019, False, "Vol. 8", "Anual"))
revistas.append(revista("005", "Revista de Software", 2023, True, "Vol. 12", "Mensual"))
revistas.append(revista("006", "Revista de Hardware", 2021, True, "Vol. 7", "Trimestral"))
revistas.append(revista("007", "Revista de Robótica", 2020, False, "Vol. 2", "Semestral"))
revistas.append(revista("008", "Revista de Inteligencia Artificial", 2022, True, "Vol. 15", "Anual"))
revistas.append(revista("009", "Revista de Ciencia de Datos", 2023, True, "Vol. 20", "Mensual"))
revistas.append(revista("010", "Revista de Ciberseguridad", 2019, False, "Vol. 1", "Trimestral"))

materiales_digitales = []
materiales_digitales.append(Material_Digital("001", "Curso de Python en PDF", 2021, True, "PDF", "http://example.com/python.pdf", 5.0))
materiales_digitales.append(Material_Digital("002", "Tutorial de Data Science en PDF", 2020, False, "PDF", "http://example.com/datascience.pdf", 10.0))
materiales_digitales.append(Material_Digital("003", "Guía de Machine Learning en PDF", 2022, True, "PDF", "http://example.com/machinelearning.pdf", 15.0))
materiales_digitales.append(Material_Digital("004", "Manual de Python para Principiantes en PDF", 2019, False, "PDF", "http://example.com/python_basico.pdf", 8.0))
materiales_digitales.append(Material_Digital("005", "Ebook de Automatización con Python en PDF", 2023, True, "PDF", "http://example.com/automatizacion.pdf", 12.0))
materiales_digitales.append(Material_Digital("006", "Curso de Python en Videos", 2021, True, "Video", "http://example.com/python_videos.mp4", 500.0))
materiales_digitales.append(Material_Digital("007", "Tutorial de Data Science en Videos", 2020, False, "Video", "http://example.com/datascience_videos.mp4", 1000.0))
materiales_digitales.append(Material_Digital("008", "Guía de Machine Learning en Videos", 2022, True, "Video", "http://example.com/machinelearning_videos.mp4", 1500.0))
materiales_digitales.append(Material_Digital("009", "Manual de Python para Principiantes en Videos", 2019, False, "Video", "http://example.com/python_basico_videos.mp4", 800.0))
materiales_digitales.append(Material_Digital("010", "Ebook de Automatización con Python en Videos", 2023, True, "Video", "http://example.com/automatizacion_videos.mp4", 1200.0))

usuarios = []
usuarios.append(usuario("Juan", "Pérez", 3, []))
usuarios.append(usuario("María", "García", 2, []))
usuarios.append(usuario("Carlos", "López", 4, []))
usuarios.append(usuario("Ana", "Martínez", 1, []))
usuarios.append(usuario("Luis", "Fernández", 5, []))
usuarios.append(usuario("Sofía", "Gómez", 3, []))
usuarios.append(usuario("Miguel", "Sánchez", 2, []))
usuarios.append(usuario("Laura", "Rodríguez", 4, []))
usuarios.append(usuario("Javier", "Torres", 1, []))
usuarios.append(usuario("Elena", "Díaz", 5, []))

bibliotecarios = []
bibliotecarios.append(bibliotecario("Ana", "García", "EMP-01"))

admin = bibliotecarios[0]

print("Lista de Libros")
for L in libros:
    print(L)
print("\n")
print("Lista de Revistas")
for R in revistas:
    print(R)
print("\n")
print("Lista de Materiales Digitales")
for MD in materiales_digitales:
    print(MD)
print("\n")
print("Lista de Usuarios")
for U in usuarios:
    print(U)
print("\n")


pruebas = [
    (usuarios[0], libros[2], 2002),
    (usuarios[1], revistas[4], 2003),
    (usuarios[2], materiales_digitales[0], 2004),
    (usuarios[3], libros[4], 2005),
    (usuarios[4], revistas[8], 2006),
    (usuarios[5], materiales_digitales[5], 2007),
    (usuarios[6], libros[7], 2008),
    (usuarios[7], revistas[2], 2009),  
    (usuarios[8], materiales_digitales[2], 2010)
]

for i, (u, m, id_p) in enumerate(pruebas, start=1):
    print(f"\nPRUEBA {i}: {u.nombre} {u.apellido} con {m.titulo}")
    
    print(f"Estado inicial material: {m}")
    print(f"Préstamos activos usuario: {len(u.listaActiva)}")

    print("\nGestion del prestamo")
    admin.gestionarPrestamo(id_p, u, m)

    print(f"\nEstado del material tras el préstamo: {m}")
    print(f"Estado del usuario tras el préstamo: {len(u.listaActiva)} elemento(s)")

    print("\nGestionando devolución")
    admin.gestionarDevolucion(m, u)

    print(f"\nEstado del material tras la devolución: {m}")
    print(f"Estado del usuario tras la devolución: {len(u.listaActiva)} elemento(s)")
