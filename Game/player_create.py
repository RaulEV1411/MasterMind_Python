from player_change import Game_select
from colored import attr, fg
import itertools
import random

class Computer_play(Game_select):
    colors = ["r", "b", "g", "y", "m", "c"]

    def start_cpu_game(self):
        turnos_jugados = 0
        combinacion = ""
        print(f"{attr('reset')}{fg('magenta')}Vamos a jugar debes crear un código secreto, escribe la primera letra del color y sepárala con 1 espacio, debes elegir 4 colores de los siguientes:\n       {fg('red')}red{fg('blue')} blue {fg('green')}green {fg('yellow')}yellow {fg('magenta')}magenta {fg('cyan')}cyan{attr('reset')}")
        combinacion_secreta = self.user_choise(self.colors)
        juego_ganado = self.validar_victoria(combinacion, combinacion_secreta)
        intentos = self.is_game_over(intentos_pendientes=turnos_jugados, jugador_gano=juego_ganado, combinacion_s=combinacion_secreta)
        while not intentos:
            combinacion = self.fuerza_bruta()
            print(f"Intentos {turnos_jugados}: Ingresa la combinación: {combinacion}")
            self.dar_pistas(combinacion, combinacion_secreta, turnos_jugados)
            turnos_jugados += 1
            juego_ganado = self.validar_victoria(combinacion, combinacion_secreta)
            intentos = self.is_game_over(intentos_pendientes=turnos_jugados, jugador_gano=juego_ganado, combinacion_s=combinacion_secreta)

    def fuerza_bruta(self):
        combinaciones_posibles = list(itertools.product(self.colors, repeat=4))
        random.shuffle(combinaciones_posibles)  
        for combinacion in combinaciones_posibles:
            return list(combinacion)


