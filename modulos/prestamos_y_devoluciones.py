""" Importamos las librerías necesarias"""
import json
import os
from datetime import datetime
from modulos.manejo_de_archivo import abrir_archivo, crear_archivo, escribir_archivo

""" Rutas de los archivos JSON"""
ruta_prestamos = os.path.join(os.path.dirname(__file__),"../datos/prestamos.json")
ruta_socios = os.path.join(os.path.dirname(__file__),"../datos/socio.json")
ruta_libros = os.path.join(os.path.dirname(__file__),"../datos/libro.json")

def iniciar_archivo_prestamos():
    """Función para crear el archivo de préstamos si no existe"""
    if not os.path.exists(ruta_prestamos):
        crear_archivo(ruta_prestamos)


def validar_socio(id_socio):
    """Función para validar si un socio existe en la base de datos """
    socios = abrir_archivo(ruta_socios)
    for socio in socios:
        if socio['id_socio'] == id_socio:
            return True
    return False


def validar_libro(id_libro):
    """ Función para validar si un libro existe en la base de datos """
    libros = abrir_archivo(ruta_libros)
    for libro in libros:
        if libro['id_libro'] == id_libro:
            return True
    return False


def obtener_libro(id_libro):
    """ Función para obtener la información de un libro por su ID """
    libros = abrir_archivo(ruta_libros)
    for libro in libros:
        if libro['id_libro'] == id_libro:
            return libro
    return None


def actualizar_libros(libros):
    """ Función para actualizar la base de datos de libros """
    escribir_archivo(ruta_libros, libros)

def validar_fecha(fecha):
    try:
        """Verificar si la fecha está en el formato correcto"""
        datetime.strptime(fecha, '%d-%m-%Y')
        return True
    except ValueError:
        return False
    

def registrar_prestamo():
    """Función para registrar un nuevo préstamo"""
    prestamos = abrir_archivo(ruta_prestamos)

   # id_prestamo = len(prestamos) + 1
    if prestamos:
        ultimo_prestamo = prestamos[-1]
        id_viejo = ultimo_prestamo["id_prestamo"]
        id_nuevo_prestamo = id_viejo + 1     
    else:
        id_nuevo_prestamo = 1
    
    id_socio = int(input("Ingrese el ID del socio: "))
    
    if not validar_socio(id_socio):
        print("ID de socio no válido.")
        return

    id_libro = int(input("Ingrese el ID del libro: "))
    libro = obtener_libro(id_libro)
    if not libro:
        print("ID de libro no válido.")
        return
    if libro['cantidad_disponible'] <= 0:
        print("No hay libros disponibles.")
        return

    while True:
        fecha_prestamo = input("Ingrese la fecha del préstamo (DD-MM-YYYY): ")
        if validar_fecha(fecha_prestamo):
            break
        else:
            print("Fecha no válida. Debe seguir el formato DD-MM-YYYY.")

    costo = float(input("Ingrese el costo (si aplica, sino 0): "))
    estado = "En Curso"

    prestamo = {
        "id_prestamo": id_nuevo_prestamo,
        "id_socio": id_socio,
        "id_libro": id_libro,
        "fecha_prestamo": fecha_prestamo,
        "costo": costo,
        "fecha_devolucion": "",
        "estado": estado
    }

    prestamos.append(prestamo)
    escribir_archivo(ruta_prestamos, prestamos)

    """Actualizar la cantidad de libros disponibles """
    libro['cantidad_disponible'] -= 1
    libros = abrir_archivo(ruta_libros)
    for i in range(len(libros)):
        if libros[i]['id_libro'] == id_libro:
            libros[i] = libro
    actualizar_libros(libros)

    print(f"Préstamo registrado con éxito: {prestamo}")


# Función para registrar la devolución de un préstamo
def registrar_devolucion():
    prestamos = abrir_archivo(ruta_prestamos)
    id_prestamo = int(input("Ingrese el ID del préstamo a devolver: "))
    
    while True:
        fecha_devolucion = input("Ingrese la fecha de devolución (DD-MM-YYYY): ")
        if validar_fecha(fecha_devolucion):
            break
        else:
            print("Fecha no válida. Debe seguir el formato DD-MM-YYYY.")

    prestamo_encontrado = False
    id_libro = None

    for prestamo in prestamos:
        if prestamo["id_prestamo"] == id_prestamo and prestamo["estado"] == "En Curso":
            prestamo["fecha_devolucion"] = fecha_devolucion
            prestamo["estado"] = "Devuelto"
            prestamo_encontrado = True
            id_libro = prestamo["id_libro"]
            print(f"Devolución registrada: {prestamo}")

    if not prestamo_encontrado:
        print("Préstamo no encontrado o ya devuelto.")
    else:
        # Aumentar la cantidad de libros disponibles
        libros = abrir_archivo(ruta_libros)
        for libro in libros:
            if libro['id_libro'] == id_libro:
                libro['cantidad_disponible'] += 1
                break
        actualizar_libros(libros)

    escribir_archivo(ruta_prestamos, prestamos)

# Función para generar un reporte de préstamos
def generar_reporte_prestamos():
    prestamos = abrir_archivo(ruta_prestamos)
    socios = abrir_archivo(ruta_socios)
    libros = abrir_archivo(ruta_libros)

    print("Seleccione el criterio para el reporte:")
    print("1. Por Socio")
    print("2. Por Libro")
    print("3. Por Rango de Fechas")
    criterio = input("Ingrese el número correspondiente al criterio: ")
    reporte = []
    if criterio == "1":
        id_socio = int(input("Ingrese el ID del socio: "))
        reporte = []
        for prestamo in prestamos:
            if prestamo["id_socio"] == id_socio:
                reporte.append(prestamo)
    elif criterio == "2":
        id_libro = int(input("Ingrese el ID del libro: "))
        reporte = []
        for prestamo in prestamos:
            if prestamo["id_libro"] == id_libro:
                reporte.append(prestamo)
    elif criterio == "3":
        print("Seleccione por cuál fecha quiere filtrar:")
        print("1. Fecha de Préstamo")
        print("2. Fecha de Devolución")
        try:
            criterio_fecha = int(input("Ingrese el número correspondiente al criterio: "))
            fecha_inicio = input("Ingrese la fecha de inicio (DD-MM-YYYY): ")
            fecha_fin = input("Ingrese la fecha de fin (DD-MM-YYYY): ")
            
            try:
                fecha_inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y")
                fecha_fin = datetime.strptime(fecha_fin, "%d-%m-%Y")
            except ValueError:
                print("Formato de fecha no válido. Use el formato DD-MM-YYYY.")
                return

            for prestamo in prestamos:
                if criterio_fecha == 1:  # Por fecha de préstamo
                    fecha_prestamo = datetime.strptime(prestamo["fecha_prestamo"], "%d-%m-%Y")
                    if fecha_inicio <= fecha_prestamo <= fecha_fin:
                        reporte.append(prestamo)
                elif criterio_fecha == 2:  # Por fecha de devolución
                    if prestamo["fecha_devolucion"]:  # Solo filtra si hay fecha de devolución
                        fecha_devolucion = datetime.strptime(prestamo["fecha_devolucion"], "%d-%m-%Y")
                        if fecha_inicio <= fecha_devolucion <= fecha_fin:
                            reporte.append(prestamo)
                else:
                    print("Criterio de búsqueda no válido.")
                    return

        except ValueError:
            print("Criterio no válido.")
            return              
    else:
        print("Criterio de búsqueda no válido.")
        return

    if reporte:
        for r in reporte:
            socio_nombre = "Desconocido"
            for socio in socios:
                if socio["id_socio"] == r["id_socio"]:
                    socio_nombre = f"{socio['id_socio']} - {socio['nombre']} {socio['apellido']}"
                    break

            libro_titulo = "Desconocido"
            for libro in libros:
                if libro["id_libro"] == r["id_libro"]:
                    libro_titulo = f"{libro['id_libro']} - {libro['titulo']}"
                    break

            print(f"ID Préstamo: {r['id_prestamo']}")
            print(f"Socio: {socio_nombre}")
            print(f"Libro: {libro_titulo}")
            print(f"Fecha de Préstamo: {r['fecha_prestamo']}")
            print(f"Fecha de Devolución: {r['fecha_devolucion']}")
            print(f"Estado: {r['estado']}")
            print(f"Costo: {r['costo']}")
            print("-" * 40)
    else:
        print("No se encontraron préstamos con los criterios proporcionados.")

# Función principal del sistema
def main_prestamos_y_devoluciones():
    iniciar_archivo_prestamos()

    print("Sistema de Gestión de Préstamos")
    accion = int(input("1: Registrar Préstamo\n2: Registrar Devolución\n3: Generar Reporte de Préstamos\n0: Salir\nSeleccione una opción: "))

    while accion != 0:
        if accion == 1:
            registrar_prestamo()
        elif accion == 2:
            registrar_devolucion()
        elif accion == 3:
            generar_reporte_prestamos()
        else:
            print("Opción no válida")

        accion = int(input("1: Registrar Préstamo\n2: Registrar Devolución\n3: Generar Reporte de Préstamos\n0: Salir\nSeleccione una opción: "))

    print("Gracias por usar el sistema de préstamos")


if __name__ == "__main__":
    main_prestamos_y_devoluciones()
