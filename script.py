import json
from usuario import Usuario
from datetime import datetime

def procesar_archivo(ruta):
    """
    Procesa un archivo de texto que contiene datos de usuarios en formato JSON.

    Esta función lee un archivo línea por línea, intenta parsear cada línea como JSON
    para crear objetos Usuario, y maneja los errores que puedan ocurrir durante el proceso.

    Args:
        ruta (str): La ruta al archivo que se va a procesar.

    Returns:
        list: Una lista de objetos Usuario creados a partir de los datos del archivo.

    Raises:
        Exception: Si hay un error al abrir o procesar el archivo.

    Note:
        Los errores se registran en un archivo 'error.log'.
    """
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
                        log.write(f"{fecha_actual} : Error al procesar usuario: {e}\n")
                finally:
                    if log is not None:
                        log.close()
    except Exception as e:
        fecha_actual = datetime.now()
        #print(fecha_actual)
        with open("error.log", "a") as log:
            log.write(f"{fecha_actual} : Error al procesar usuario: {e}\n")
    finally:
        if archivo is not None:
            archivo.close()
    return usuarios

procesar_archivo("usuarios.txt")
