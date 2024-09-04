import json

from usuario import Usuario

ruta = 'usuarios.txt'

def procesar_archivo():
    usuarios = []
    with open(ruta, "r") as archivo:
        for linea in archivo:
            try:
               
                datos_usuario = json.loads(linea)  # guarda los datos de una línea en formato JSON

                    usuario = Usuario(
                    nombre=datos_usuario["nombre"],
                    apellido=datos_usuario["apellidos"],
                    email=datos_usuario["email"],
                    genero=datos_usuario["genero"]
                )
                usuarios.append(usuario)
            except Exception as e:
                
                with open("error.log", "a") as log:
                    log.write(f"Error al procesar usuario: {e}\n")
    return usuarios
