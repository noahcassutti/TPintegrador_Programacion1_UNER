from modulos.libros import *
from modulos.libros import (agregar_libros, eliminar_libro, editar_libro, buscar_libro_titulo_genero_autor_editoral)
from modulos.libros import main_libros

from modulos.socios import (main_socios, agregar_socio, eliminar_socio, editar_socio, buscar_socio_id_nombre_apellido)

from modulos.qrcode import *
from modulos.qrcode import qr_biblioteca

from modulos.prestamos_y_devoluciones import *
from modulos.prestamos_y_devoluciones import main_prestamos_y_devoluciones




def menu():
    print("Bienvenido a la biblioteca")
    print("1. Gestion de libros")
    print("2. Gestion de Socios")
    print("3. Gestion de Prestamos y Devoluciones")
    print("4. QR biblioteca")
    print("5. Salir")

def main():
    while True:

        menu()
        opcion = int(input("Ingrese una opcion con 5 finaliza: "))
        if opcion == 1:
            main_libros()
            
        elif opcion == 2:
            main_socios()
        elif opcion == 3:
            main_prestamos_y_devoluciones()
        elif opcion == 4:
             # recordar instalar pip install pyqrcode para que se genere el qr
            print("\n Se ha generado correctamente el QR de biblioteca en formato svg, escaneando con el celular podra ingresar! \n")
            qr_biblioteca()
            

        elif opcion == 5:
            print("Gracias por usar nuestro sistema")
            break
        else:
            print("Ingrese una opcion valida")
            main()

if __name__ == "__main__":
    main()