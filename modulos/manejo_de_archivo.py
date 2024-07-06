import json
import os



def abrir_archivo(ruta):
    if os.path.exists(ruta) == False:
        return False
    archivo=open(ruta,'r',encoding='utf-8')

    contenido = archivo.read()
    obj_json = json.loads(contenido)

    archivo.close()
    return obj_json
def crear_archivo(ruta):
    """ Revisar si el archivo existe para no sobreescribir datos"""
    if os.path.exists(ruta) == True:
        return ruta
    archivo = open(ruta,'w',encoding='utf-8')
    lista_vacia = []
    """inicializar el archivo con algo"""
    string_lista = json.dumps(lista_vacia)

    """ se escribe ese algo"""

    archivo.write(string_lista)
    """se cierra el archivo"""
    
    archivo.close()
    
    return ruta

def escribir_archivo(ruta, datos):
    #if os.path.exists(ruta) == True:
         #return ruta
    
    archivo = open(ruta,'w',encoding='utf-8')
    string_Datos = json.dumps(datos, ensure_ascii=False, indent=4)

    archivo.write(string_Datos)
    
    archivo.close()

    return True

