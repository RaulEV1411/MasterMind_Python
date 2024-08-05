from colored import fg,attr

class Board:
    def __init__(self) -> None:
        self.arrays_tablero =  [["O","O","O","O",["o","o","o","o"]] for _ in range(12)]

    def añadir_al_array(self,valores_agregar,posicion_tablero, array_ayudas):
        self.arrays_tablero[posicion_tablero] = valores_agregar, array_ayudas

    def mostrar_al_array(self):
        for element in self.arrays_tablero:
            print("|  " + "  ".join(map(str, element)) + "|")

