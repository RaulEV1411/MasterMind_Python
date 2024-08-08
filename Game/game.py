import player_change
import player_create

usuario_elige = player_change.Game_select()
usuario_crea = player_create.Computer_play()

class Game:
    def jugar(self):
        nombre = input("Agrega tu nombre: ")
        print(f"¡Bienvenido a Mastermind, {nombre}! \n Vamos a comenzar,si quieres adivinar presiona [a] si quieres crear el codigo presiona [c].")
        opciones_disponibles = ["a","c"]
        while True:
            combinacion = input("").lower().split()
            if all(opciones in opciones_disponibles for opciones in combinacion):
                if combinacion == ["a"]:
                    usuario_elige.star_game()
                    return
                elif combinacion == ["c"]:
                    usuario_crea.start_cpu_game()
                    return
            else:
                print("Ese dato no es una respuesta")
            

juego = Game()
juego.jugar()