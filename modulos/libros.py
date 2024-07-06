import json
import os

from modulos.manejo_de_archivo import abrir_archivo
from modulos.manejo_de_archivo import crear_archivo
from modulos.manejo_de_archivo import escribir_archivo


def listar_libros(ruta):

    libros = abrir_archivo(ruta)
    for libro in libros:
        print(libro)


def agregar_libros(ruta):

    libros = abrir_archivo(ruta)
    quiere_salir = False
    print("Agregar libros: ")
    while quiere_salir == False:
        """ Obtener el ID de libr más alto"""
        if libros:
            ultimo_libro = libros[-1]
            id_viejo = ultimo_libro["id_libro"]
            id_nuevo_libro = id_viejo + 1     
        else:
            id_nuevo_libro = 1
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        editorial= input("Ingrese la editorial del libro: ")
        año_publicacion = int(input("Ingrese el año del libro: "))
        genero = input("Ingrese el genero del libro: ")
        cantidad_disponible =  int(input("Ingrese la cantidad disponible: "))

        libro = {
            "id_libro": id_nuevo_libro,
            "titulo": titulo,
            "autor": autor,
            "editorial": editorial,
            "año_publicacion": año_publicacion,
            "genero": genero,
            "cantidad_disponible": cantidad_disponible
                
        }

        libros.append(libro)

        salir = input("Escribe 'SI' si quiere salir, de lo contrario cualquier tecla: ")

        if salir == "SI" or salir == "si":
            quiere_salir = True
    escribir_archivo(ruta, libros)

def eliminar_libro(ruta):

    libros = abrir_archivo(ruta)
    id_libro = int(input("Ingrese el id del libro a eliminar: "))

    for libro in libros:
        if libro['id_libro'] == id_libro:
            libros.remove(libro)
            print("Se ha elimiado exitosamente!")
    escribir_archivo(ruta, libros)


"""Búsqueda de libros por id, título, género, autor y editorial 
 se agrega funcionalidad """
def buscar_libro_titulo_genero_autor_editoral(ruta):

    libros = abrir_archivo(ruta)
    

   
    escribir_archivo(ruta, libros)
    print("Seleccione el criterio de búsqueda:")
    print("1. ID")
    print("2. Titulo")
    print("3. Genero")
    print("4. Autor")
    print("5. Editorial")
          
    criterio = input("Ingrese el número correspondiente al criterio: ")
    libro_encontrado = False
   
    if criterio == "1":
        valor = int(input("Ingrese el id del socio a buscar: "))
        
        for libro in libros:
            if libro['id_libro'] == valor:
                libro_encontrado = True
                print(libro)

    elif criterio == "2":
        valor = input("Ingrese el titulo a buscar: ").strip().lower()
        for libro in libros:
            if libro["titulo"].lower() == valor:
                libro_encontrado = True
                print(libro)
                
    
    elif criterio == "3":
        valor = input("Ingrese el genero a buscar: ").strip().lower()
        for libro in libros:
            if libro["genero"].lower() == valor:
                libro_encontrado = True
                print(libro)

    elif criterio == "4":
        valor = input("Ingrese el autor a buscar: ").strip().lower()
        for libro in libros:
            if libro["autor"].lower() == valor:
                libro_encontrado = True
                print(libro)

    elif criterio == "5":
        valor = input("Ingrese la editorial a buscar: ").strip().lower()
        for libro in libros:
            if libro["editorial"].lower() == valor:
                libro_encontrado = True
                print(libro)
    else:
        print("Criterio de búsqueda no válido.")

    if libro_encontrado == False:
        print("Libro no encontrado")

    escribir_archivo(ruta, libros)

def editar_libro(ruta):
    libros = abrir_archivo(ruta)

    id_libro = int(input("Ingrese el id del libro a editar: "))
    libro_encontrado = False
    for libro in libros:
        if libro['id_libro'] == id_libro:
            libro_encontrado = True
            print(libro)
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor del libro: ")
            editorial= input("Ingrese la editorial del libro: ")
            año_publicacion = int(input("Ingrese el año del libro: "))
            genero = input("Ingrese el genero del libro: ")
            cantidad_disponible =  int(input("Ingrese la cantidad disponible: "))
            libro['titulo'] = titulo
            libro['autor'] = autor
            libro['editorial'] = editorial
            libro['año_publicacion'] = año_publicacion
            libro['genero'] = genero
            libro['cantidad_disponible'] = cantidad_disponible
    if libro_encontrado == True:
        escribir_archivo(ruta, libros)
    else:
        print("Libro no encontrado")

ruta = os.path.join(os.path.dirname(__file__),"../datos/libro.json")

libros = abrir_archivo(ruta)

if libros == False:
    crear_archivo(ruta)
    libros = abrir_archivo(ruta)

#print(libros)
 #print(f"Tamanio de libros: {(len(libros))}")


def main_libros():
    print ("Que queres hacer?")
    accion_usuario = int(input("\n 1: Listar libros \n 2: Agregar Libro \n 3: Borrar Libro \n 4: Buscar Libro por Id/titulo/genero/autor/editorial \n 5: Editar Libro \n 0: Salir \n"))

    while accion_usuario != 0:

        match accion_usuario:
            case 1:
                listar_libros(ruta)
            case 2:
                agregar_libros(ruta)
            case 3:
                eliminar_libro(ruta)
            case 4:
                buscar_libro_titulo_genero_autor_editoral(ruta)

            case 5:
                editar_libro(ruta)

            case 0:
                print("Gracias por usar nuestro programa")

        accion_usuario = int(input("\n 1: Listar libros \n 2: Agregar Libro \n 3: Borrar Libro \n 4: Buscar Libro por Id/titulo/genero/autor/editorial \n 5: Editar Libro \n 0: Salir \n"))

if __name__ == "__main__":
    main_libros





