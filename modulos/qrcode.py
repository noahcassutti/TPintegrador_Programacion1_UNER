import pyqrcode 

def qr_biblioteca():
    qr = pyqrcode.create('Bienvenidos a nuestra biblioteca! \n Direccion: Cordoba, Cordobita, 1300 \n Telefono: 123456789 \n correo electronico de la biblioteca: biblioteca@gmail.com \n Paginan web: bibliotecafalsa.com \n')
    qr.svg('biblioteca.svg')


if __name__ == '__main__':
    qr_biblioteca()