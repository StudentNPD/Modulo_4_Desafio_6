class Usuario:
    """
    Representa un usuario con información básica.

    Esta clase almacena los datos principales de un usuario, incluyendo
    su nombre, apellidos, correo electrónico y género.

    Attributes:
        nombre (str): El nombre del usuario.
        apellidos (str): Los apellidos del usuario.
        email (str): La dirección de correo electrónico del usuario.
        genero (str): El género del usuario.
    """

    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        """
        Inicializa una nueva instancia de Usuario.

        Args:
            nombre (str): El nombre del usuario.
            apellido (str): El apellido del usuario.
            email (str): La dirección de correo electrónico del usuario.
            genero (str): El género del usuario.
        """
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellidos}, Email: {self.email}, Género: {self.genero}"