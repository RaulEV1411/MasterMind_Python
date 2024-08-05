import player_change

usuario_elige = player_change.Game_select()

class Game:
    def jugar(self):
        nombre = input("Agrega tu nombre")
        print(f"¡Bienvenido a Mastermind, {nombre}! \n Vamos a comenzar,si quieres adivinar presiona [a] si quieres crear el codigo presiona [c].")
        modo_juego = usuario_elige.user_choise(["a","b"])
        if modo_juego == ["a"]:
            usuario_elige.star_game()
        else:
            print("espera")
            

juego = Game()
juego.jugar()