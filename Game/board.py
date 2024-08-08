class Board:
    def __init__(self) -> None:
        # Inicializa el tablero con 12 filas de 4 posiciones cada una, llenas de "O"
        # Inicializa el tablero de ayudas con 12 filas de 4 posiciones cada una, llenas de "o"
        self.arrays_tablero = [["O", "O", "O", "O"] for _ in range(12)]
        self.arrays_de_ayuda = [["o", "o", "o", "o"] for _ in range(12)]

    # Añade una combinación de colores y las ayudas correspondientes al tablero en una posición específica
    def añadir_al_array(self, valores_agregar, posicion_tablero, array_ayudas):
        # Actualiza la fila del tablero con los valores proporcionados por el usuario
        self.arrays_tablero[posicion_tablero] = valores_agregar
        # Actualiza la fila de ayudas con las pistas generadas
        self.arrays_de_ayuda[posicion_tablero] = array_ayudas

    # Muestra el estado actual del tablero, incluyendo las combinaciones del usuario y las ayudas
    def mostrar_al_array(self):
        # Itera sobre cada fila del tablero y la correspondiente fila de ayudas
        for fila_tablero, fila_ayuda in zip(self.arrays_tablero, self.arrays_de_ayuda):
            # Convirtiendo cada elemento de ambas filas a string y uniéndolos con espacios
            fila_tablero_str = "  ".join(map(str, fila_tablero))
            fila_ayuda_str = "  ".join(map(str, fila_ayuda))
            # Imprimiendo la fila combinada del tablero y las ayudas
            print(f"|  {fila_tablero_str}  |  {fila_ayuda_str}  |")
