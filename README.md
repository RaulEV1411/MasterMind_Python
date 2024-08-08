# MasterMind_Python

Descripción General:
El código implementa una versión del juego Mastermind. El usuario puede elegir entre dos modos de juego: adivinar un código secreto generado por la computadora o crear un código secreto que la computadora intentará adivinar.

Clases Principales:
Game_select (módulo player_change):

Función: Gestiona el juego en el modo de adivinanza.
Métodos Clave:
combinacion(): Genera una combinación secreta.
is_game_over(): Verifica si el juego ha terminado.
validar_victoria(): Verifica si la combinación del usuario es correcta.
dar_pistas(): Proporciona pistas sobre la combinación.
user_choise(): Solicita una combinación de colores del usuario.
star_game(): Inicia el juego.
Computer_play (módulo player_create):

Función: Gestiona el juego en el modo en el que la computadora adivina el código secreto.
Método Clave:
start_cpu_game(): Inicia el juego de adivinanza por la computadora.
Board (módulo board):

Función: Administra y muestra el estado del tablero de juego.
Métodos Clave:
añadir_al_array(): Añade combinaciones y pistas al tablero.
mostrar_al_array(): Muestra el estado del tablero.
Game:

Función: Controla la interacción del usuario y permite elegir entre los modos de juego.
Método Clave:
jugar(): Maneja la entrada del usuario y comienza el juego.
Paquetes Utilizados:
random:

Genera combinaciones aleatorias.
colored:

Añade colores y formato al texto en la consola.
board:

Contiene la clase Board para la visualización del juego.
player_change:

Contiene la clase Game_select para el modo de adivinanza.
player_create:

Contiene la clase Computer_play para el modo de creación de código.
Funcionamiento Global:
Inicio del Juego:

El usuario inicia el juego a través de la clase Game.
Selección del Modo:

El usuario elige entre adivinar un código o crear uno.
Modo de Adivinanza:

Usa Game_select para manejar el juego.
Modo de Creación:

Usa Computer_play para manejar el juego.
Visualización:

Usa Board para mostrar el estado del juego.
