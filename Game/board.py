
class Board:
    def __init__(self) -> None:
        self.arrays_tablero =  [["O","O","O","O"] for _ in range(12)]
        self.arrays_de_ayuda = [["o","o","o","o"] for _ in range(12)]

    def añadir_al_array(self,valores_agregar,posicion_tablero, array_ayudas):
        self.arrays_tablero[posicion_tablero] = valores_agregar
        self.arrays_de_ayuda[posicion_tablero] = array_ayudas

    def mostrar_al_array(self):
        for fila_tablero, fila_ayuda in zip(self.arrays_tablero, self.arrays_de_ayuda):
            # Convirtiendo cada elemento de ambas filas a string
            fila_tablero_str = "  ".join(map(str, fila_tablero))
            fila_ayuda_str = "  ".join(map(str, fila_ayuda))
            # Imprimiendo la fila combinada
            print(f"|  {fila_tablero_str}  |  {fila_ayuda_str}  |")
