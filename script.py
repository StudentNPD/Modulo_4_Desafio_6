import json

from usuario import Usuario
from datetime import datetime


def procesar_archivo(ruta):
    usuarios = []
    archivo = None
    log = None
   
    try:
        with open(ruta, "r") as archivo:
            for linea in archivo:
                try:
                    datos_usuario = json.loads(linea)  # guarda los datos de una línea en formato JSON
                    usuario = Usuario(
                    nombre=datos_usuario["nombre"],
                    apellido=datos_usuario["apellido"],
                    email=datos_usuario["email"],
                    genero=datos_usuario["genero"]
                    )
                    usuarios.append(usuario)
                except Exception as e:
                    fecha_actual = datetime.now()
                    with open("error.log", "a") as log:
                        log.write(f"Error al procesar usuario: {e}\n")
                finally:
                    if log is not None:
                        log.close()
    except Exception as e:
        fecha_actual = datetime.now()
        #print(fecha_actual)
        with open("error.log", "a") as log:
            log.write(f"Error al procesar usuario: {e}\n")
    finally:
        if archivo is not None:
            archivo.close()
    return usuarios



procesar_archivo("usuarios.txt")
