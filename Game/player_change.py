import board
from colored import fg, attr

import random
tablero = board.Board()

class Game_select:

    def combinacion(self):
        self.colors = ["r", "b", "g", "y","m","c"]
        self.combinacion_secreta = random.sample(self.colors, k=4)
        return self.combinacion_secreta

    def is_game_over(self,intentos_pendientes: int, jugador_gano: bool) -> bool :
        if  jugador_gano == True:
            return True
        elif intentos_pendientes >= 12 :
            tablero.mostrar_al_array()
            print(f"Te has quedado sin intentos el codigo secreto era {self.combinacion_secreta}")
            return True
        else: 
            return False
 
    def validar_victoria(self,combinacion_user,combinacion_secreta):
        if combinacion_user == combinacion_secreta:
            tablero.mostrar_al_array()
            print("Felicidades has descubierto el codigo secreto")
            return True
        else:
            return False

    def dar_pistas(self,combinacion_user,combinacion_secreta,turno):
        array_ayudas = ["","","",""]
        for i in range(4):
            if combinacion_user[i] == combinacion_secreta[i]:
                array_ayudas[i] = f"{attr('reset')}{fg('green')}o{attr('reset')}"
            elif combinacion_user[i] in combinacion_secreta and combinacion_user[i] != combinacion_secreta[i]:
                array_ayudas[i] = f"{attr('reset')}{fg('red')}o{attr('reset')}"
            else:
                array_ayudas[i] = f"o"
        tablero.añadir_al_array(combinacion_user,turno,array_ayudas)
        return

    def user_choise(self,opciones_disponibles):
        while True:
            combinacion = input("").lower().split()
            if len(combinacion) == 4 and all(opciones in opciones_disponibles for opciones in combinacion):
                return combinacion
            else:
                print("Ese dato no es una respuesta")

    def star_game(self) -> None:
        turnos_jugados = 0
        combinacion = ""
        combinacion_secreta = self.combinacion()
        juego_ganado = self.validar_victoria(combinacion,combinacion_secreta)
        intentos = self.is_game_over(intentos_pendientes=turnos_jugados,jugador_gano=juego_ganado)
        while (not intentos):
            tablero.mostrar_al_array()
            print(f"{attr('reset')}{fg('magenta')}Vamos a jugar, escribe la primera letra del color y separala con 1 espacio, debes elegir 4 colores de los siguientes:\n       {fg('red')}red{fg('blue')} blue {fg('green')}green {fg('yellow')}yellow {fg('magenta')}magenta {fg('cyan')}cyan{attr('reset')}")
            print(combinacion_secreta)
            print("====================================")
            print(f"Intentos {turnos_jugados}: Ingresa la combinacion: ")
            combinacion = self.user_choise(self.colors)
            self.dar_pistas(combinacion,combinacion_secreta,turnos_jugados)
            turnos_jugados += 1
            juego_ganado = self.validar_victoria(combinacion,combinacion_secreta)
            intentos = self.is_game_over(intentos_pendientes= turnos_jugados,jugador_gano= juego_ganado)


