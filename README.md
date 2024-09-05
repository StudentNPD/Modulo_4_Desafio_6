# Desafío - Instancias de Usuario

Este proyecto implementa un script Python para crear instancias de usuario a partir de datos proporcionados en un archivo de texto, manejando excepciones y registrando errores.

## Descripción

El script lee datos de usuario desde un archivo de texto (`usuarios.txt`), crea instancias de la clase `Usuario` para cada entrada válida, y maneja las excepciones que puedan ocurrir durante el proceso.

## Estructura del Proyecto

- `script.py`: Script principal para procesar el archivo de usuarios.
- `usuario.py`: Definición de la clase `Usuario`.
- `usuarios.txt`: Archivo de entrada con datos de usuario en formato JSON.
- `error.log`: Archivo de registro para excepciones encontradas.

## Componentes Principales

### Clase `Usuario` (en `usuario.py`)

```python
class Usuario:
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero
```

Atributos:
- `nombre`: Nombre del usuario.
- `apellidos`: Apellidos del usuario.
- `email`: Correo electrónico del usuario.
- `genero`: Género del usuario.

### Función `procesar_archivo` (en `script.py`)

```python
def procesar_archivo(ruta):
    # ... (implementación)
```

Parámetros:
- `ruta`: Ruta al archivo de texto con datos de usuarios.

Funcionalidad:
- Lee el archivo línea por línea.
- Intenta crear una instancia de `Usuario` para cada línea.
- Maneja excepciones y las registra en `error.log`.
- Retorna una lista de instancias de `Usuario` creadas exitosamente.

## Flujo de Ejecución

1. El script lee `usuarios.txt`.
2. Para cada línea en el archivo:
   - Intenta parsear el JSON.
   - Crea una instancia de `Usuario` si es exitoso.
   - Captura y registra cualquier excepción en `error.log`.
3. Retorna la lista de usuarios creados.

## Manejo de Errores

- Las excepciones se capturan tanto a nivel de procesamiento de línea como a nivel de archivo.
- Todos los errores se registran en `error.log` con la fecha y hora actual.

## Uso

Para ejecutar el script:

```
python script.py
```

Asegúrate de que `usuarios.txt` esté en el mismo directorio que `script.py`.

## Requerimientos

1. Python 3.x
2. Archivo `usuarios.txt` con datos de usuario en formato JSON (una entrada por línea).

## Notas Adicionales

- El script maneja robustamente las excepciones para asegurar que el procesamiento continúe incluso si se encuentran errores en entradas individuales.
- Se recomienda revisar `error.log` después de la ejecución para verificar cualquier problema con los datos de entrada.

------------------------------------------

## Prerequisitos

- Sistema Operativos: Windows 10, 11, Linux, iOS
- Python 3.12

## Ejecución

***Windows***

`python script.py`

***Linux & iOS***

`python3 script.py`

------------------------------------------
## Colaboradores
- [Francisco Colomer](https://github.com/Cy5k0) 
- [Francisco Monroy](https://github.com/fmonroy75)
- [Natalia Peña](https://github.com/StudentNPD)
