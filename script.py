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

    Note:
        Los errores se registran en un archivo 'error.log'.
    """
    usuarios = []
   
    try:
        with open(ruta, "r") as archivo:
            for numero_linea, linea in enumerate(archivo, 1):
                try:
                    datos_usuario = json.loads(linea.strip())
                    usuario = Usuario(
                        nombre=datos_usuario["nombre"],
                        apellido=datos_usuario["apellido"],
                        email=datos_usuario["email"],
                        genero=datos_usuario["genero"]
                    )
                    usuarios.append(usuario)
                except json.JSONDecodeError as e:
                    log_error(f"Error de JSON en línea {numero_linea}: {e}")
                except KeyError as e:
                    log_error(f"Falta clave en datos de usuario en línea {numero_linea}: {e}")
                except Exception as e:
                    log_error(f"Error al procesar usuario en línea {numero_linea}: {e}")
    except FileNotFoundError:
        log_error(f"No se encontró el archivo: {ruta}")
    except Exception as e:
        log_error(f"Error al abrir o leer el archivo: {e}")

    return usuarios

def log_error(mensaje):
    """
    Registra un mensaje de error en el archivo error.log.

    Args:
        mensaje (str): El mensaje de error a registrar.
    """
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("error.log", "a") as log:
        log.write(f"{fecha_actual} - {mensaje}\n")

if __name__ == "__main__":
    ruta_archivo = "usuarios.txt"
    usuarios_procesados = procesar_archivo(ruta_archivo)
    print(f"Se procesaron {len(usuarios_procesados)} usuarios correctamente.")