import board
from colored import fg, attr
import random

# Creación de una instancia del tablero de juego
tablero = board.Board()

class Game_select:

    # Genera una combinación secreta de 4 colores seleccionados aleatoriamente
    # Se eligen 4 colores distintos de la lista de colores disponibles.
    def combinacion(self):
        self.colors = ["r", "b", "g", "y", "m", "c"]
        self.combinacion_secreta = random.sample(self.colors, k=4)
        return self.combinacion_secreta

    # Verifica si el juego ha terminado, ya sea porque el jugador ha ganado
    # o porque se han agotado los intentos permitidos (12 intentos).
    def is_game_over(self, intentos_pendientes: int, jugador_gano: bool, combinacion_s) -> bool:
        if jugador_gano:
            # El jugador ha ganado el juego.
            return True
        elif intentos_pendientes >= 12:
            # El jugador ha agotado los 12 intentos permitidos.
            tablero.mostrar_al_array()
            print(f"Te has quedado sin intentos, el código secreto era {combinacion_s}")
            return True
        else:
            # El juego continúa.
            tablero.mostrar_al_array()
            return False

    # Comprueba si la combinación ingresada por el jugador coincide exactamente
    # con la combinación secreta generada al inicio del juego.
    def validar_victoria(self, combinacion_user, combinacion_secreta):
        if combinacion_user == combinacion_secreta:
            tablero.mostrar_al_array()
            print("Felicidades, has descubierto el código secreto")
            return True
        else:
            return False

    # Proporciona pistas al jugador sobre cuántos colores ha acertado.
    # Un "o" verde indica un color en la posición correcta,
    # un "o" rojo indica un color correcto en la posición incorrecta,
    # y un "o" blanco indica un color incorrecto.
    def dar_pistas(self, combinacion_user, combinacion_secreta, turno):
        color_map = {
            "r": fg("red"),
            "b": fg("blue"),
            "g": fg("green"),
            "y": fg("yellow"),
            "m": fg("magenta"),
            "c": fg("cyan")
        }
        array_ayudas = ["", "", "", ""]
        array_coloreado = ["","","",""]
        for i in range(4):
            array_coloreado[i] = f"{color_map[combinacion_user[i]]}O{attr('reset')}"
            if combinacion_user[i] == combinacion_secreta[i]:
                array_ayudas[i] = f"{attr('reset')}{fg('green')}o{attr('reset')}"
            elif combinacion_user[i] in combinacion_secreta:
                array_ayudas[i] = f"{attr('reset')}{fg('red')}o{attr('reset')}"
            else:
                array_ayudas[i] = "o"
        # Añade la combinación del usuario y las pistas generadas al tablero de juego.
        tablero.añadir_al_array(array_coloreado, turno, array_ayudas)

    # Solicita al usuario que ingrese una combinación válida de colores.
    # La combinación debe consistir en 4 colores, cada uno representado por la primera letra de su nombre.
    # Los colores válidos están definidos en la lista de colores disponibles.
    def user_choise(self, opciones_disponibles):
        while True:
            combinacion = input("").lower().split()
            if len(combinacion) == 4 and all(opciones in opciones_disponibles for opciones in combinacion):
                return combinacion
            else:
                print("Ese dato no es una respuesta válida")

    # Inicia el juego, controlando el flujo principal del mismo.
    # Genera la combinación secreta y entra en un bucle que continúa hasta que el juego termina.
    # En cada iteración, muestra el tablero, solicita una combinación del usuario, da pistas,
    # y verifica si el juego ha terminado.
    def star_game(self) -> None:
        turnos_jugados = 0
        combinacion = ""
        combinacion_secreta = self.combinacion()
        juego_ganado = self.validar_victoria(combinacion, combinacion_secreta)
        intentos = self.is_game_over(intentos_pendientes=turnos_jugados, jugador_gano=juego_ganado, combinacion_s=combinacion_secreta)
        
        while not intentos:
            print(f"{attr('reset')}{fg('magenta')}Vamos a jugar, escribe la primera letra del color y sepárala con un espacio. Debes elegir 4 colores de los siguientes:\n       {fg('red')}red {fg('blue')}blue {fg('green')}green {fg('yellow')}yellow {fg('magenta')}magenta {fg('cyan')}cyan{attr('reset')}")
            print(combinacion_secreta)
            print("====================================")
            print(f"Intentos {turnos_jugados}: Ingresa la combinación: ")
            combinacion = self.user_choise(self.colors)
            self.dar_pistas(combinacion, combinacion_secreta, turnos_jugados)
            turnos_jugados += 1
            juego_ganado = self.validar_victoria(combinacion, combinacion_secreta)
            intentos = self.is_game_over(intentos_pendientes=turnos_jugados, jugador_gano=juego_ganado, combinacion_s=combinacion_secreta)
