from modulos.manejo_de_archivo import abrir_archivo, crear_archivo, escribir_archivo
from datetime import datetime
import os
import json

def listar_socios(ruta):

    socios = abrir_archivo(ruta)
    for socio in socios:
        print(socio)

def validar_fecha(fecha):
    try:
        """Verificar si la fecha está en el formato correcto"""
        datetime.strptime(fecha, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def agregar_socio(ruta):

    socios = abrir_archivo(ruta)
    quiere_salir = False
    print("Agregar socios: ")
    while quiere_salir == False:
        """ Obtener el ID de socio más alto """
        if socios:
            ultimo_socio = socios[-1]
            id_viejo = ultimo_socio["id_socio"]
            id_nuevo_socio = id_viejo + 1     
        else:
            id_nuevo_socio = 1
        nombre = input("Ingrese el nombre del socio: ")
        apellido = input("Ingrese el apellido del socio: ")
        
        while True:
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del socio (DD-MM-YYYY): ")
            if validar_fecha(fecha_nacimiento):
                break
            else:
                print("Fecha no válida. Debe seguir el formato DD-MM-YYYY.")
        direccion = input("Ingrese la dirección del socio: ")
        correo_electronico = input("Ingrese el correo electrónico del socio: ")
        telefono = input("Ingrese el teléfono del socio: ")

        socio = {
            "id_socio": id_nuevo_socio,
            "nombre": nombre,
            "apellido": apellido,
            "fecha_nacimiento": fecha_nacimiento,
            "direccion": direccion,
            "correo_electronico": correo_electronico,
            "telefono": telefono,
        }
        socios.append(socio)

        salir = input("Escribe 'SI' si quiere salir, de lo contrario cualquier tecla: ")

        if salir == "SI" or salir == "si":
            quiere_salir = True
    escribir_archivo(ruta, socios)

def eliminar_socio(ruta):

    socios = abrir_archivo(ruta)
    id_socio = int(input("Ingrese el id del socio a eliminar: "))

    for socio in socios:
        if socio['id_socio'] == id_socio:
            socios.remove(socio)
            print("Se ha eliminado exitosamente!")
            

    escribir_archivo(ruta, socios)



def editar_socio(ruta):
    socios = abrir_archivo(ruta)
    id_socio = int(input("Ingrese el id del socio a editar: "))
    socio_encontrado = False
    for socio in socios:
        if socio['id_socio'] == id_socio:
            socio_encontrado = True
            print(socio)
            nombre = input("Ingrese el nombre del socio: ")
            apellido = input("Ingrese el apellido del socio: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del socio (DD-MM-YYYY): ")
            direccion = input("Ingrese la dirección del socio: ")
            correo_electronico = input("Ingrese el correo electrónico del socio: ")
            telefono = input("Ingrese el teléfono del socio: ")
            socio['nombre'] = nombre
            socio['apellido'] = apellido
            socio['fecha_nacimiento'] = fecha_nacimiento
            socio['direccion'] = direccion
            socio['correo_electronico'] = correo_electronico
            socio['telefono'] = telefono
    if socio_encontrado == True:        
        escribir_archivo(ruta, socios)
    else:
        print("Socio no encontrado")


"""Búsqueda de socios por id, nombre y apellido 
 se agrega funcionalidad que no se pedia"""
def buscar_socio_id_nombre_apellido(ruta):

    socios = abrir_archivo(ruta)
    

   
    escribir_archivo(ruta, socios)
    print("Seleccione el criterio de búsqueda:")
    print("1. ID")
    print("2. Nombre")
    print("3. Apellido")
    criterio = input("Ingrese el número correspondiente al criterio: ")
    socio_encontrado = False
   
    if criterio == "1":
        valor = int(input("Ingrese el id del socio a buscar: "))
        
        for socio in socios:
            if socio['id_socio'] == valor:
                socio_encontrado = True
                print(socio)

    

    elif criterio == "2":
        valor = input("Ingrese el nombre a buscar: ").strip().lower()
        for socio in socios:
            if socio["nombre"].lower() == valor:
                socio_encontrado = True
                print(socio)
                
    
    elif criterio == "3":
        valor = input("Ingrese el apellido a buscar: ").strip().lower()
        for socio in socios:
            if socio["apellido"].lower() == valor:
                socio_encontrado = True
                print(socio)

    else:
        print("Criterio de búsqueda no válido.")

    if socio_encontrado == False:
        print("Socio no encontrado")

    escribir_archivo(ruta, socios)






global ruta
ruta = os.path.join(os.path.dirname(__file__),"../datos/socio.json")

socios = abrir_archivo(ruta)

if socios == False:
    crear_archivo(ruta)
    socios = abrir_archivo(ruta)

#print(socios)
#print(f"Tamanio de libros: {(len(socios))}")


def main_socios():
    print ("que queres hacer")
    accion_usuario = int(input("\n 1: Listar socios \n 2: Agregar socios \n 3: Borrar socio \n 4: Buscar socio por Id/nombre/apellido \n 5: Editar Socio  \n 0: Salir \n "))

    while accion_usuario != 0:

        match accion_usuario:
            case 1:
                listar_socios(ruta)
            case 2:
                agregar_socio(ruta)
            case 3:
                eliminar_socio(ruta)
            case 4:

               buscar_socio_id_nombre_apellido(ruta)
            case 5:
                editar_socio(ruta)
                
            case 0:
                print("Gracias por usar nuestro programa")
        accion_usuario = int(input("\n 1: Listar socios \n 2: Agregar socios \n 3: Borrar socio \n 4: Buscar socio por Id/nombre/apellido \n 5: Editar Socio  \n 0: Salir \n"))

if __name__ == "__main__":
    main_socios()


