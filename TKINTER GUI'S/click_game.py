import turtle
import random
import time

# --- CONFIGURACIÓN DE VENTANA ---
wn = turtle.Screen()
wn.title("🎯 Juego de Reflejos (con START/STOP)")
wn.bgcolor("black")
wn.setup(width=600, height=500)
wn.tracer(0)

# --- VARIABLES GLOBALES ---
score = 0
jugando = False
inicio = 0
duracion = 30  # segundos de juego

# --- TEXTOS ---
texto = turtle.Turtle()
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 200)
texto.write("Puntaje: 0", align="center", font=("Arial", 20, "bold"))

# --- OBJETIVO ---
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.hideturtle()

# --- BOTONES ---
boton = turtle.Turtle()
boton.hideturtle()
boton.penup()

def dibujar_boton(x, y, color, texto):
    boton.goto(x - 50, y - 25)
    boton.color(color)
    boton.begin_fill()
    for _ in range(2):
        boton.forward(100)
        boton.left(90)
        boton.forward(50)
        boton.left(90)
    boton.end_fill()
    boton.goto(x, y - 10)
    boton.color("black")
    boton.write(texto, align="center", font=("Arial", 14, "bold"))

def dibujar_botones():
    boton.clear()
    dibujar_boton(-120, -200, "lime", "START")
    dibujar_boton(120, -200, "red", "STOP")

dibujar_botones()

# --- FUNCIONES DE JUEGO ---
def mover_objetivo():
    """Coloca el objetivo en una posición aleatoria"""
    x = random.randint(-250, 250)
    y = random.randint(-150, 150)
    target.goto(x, y)

def actualizar_texto():
    texto.clear()
    texto.write(f"Puntaje: {score}", align="center", font=("Arial", 20, "bold"))

def clic_general(x, y):
    global jugando, score, inicio

    # Clic en START
    if -170 < x < -70 and -225 < y < -175 and not jugando:
        jugando = True
        score = 0
        inicio = time.time()
        target.showturtle()
        mover_objetivo()
        actualizar_texto()
        loop_juego()
        return

    # Clic en STOP
    if 70 < x < 170 and -225 < y < -175 and jugando:
        detener_juego()
        return

    # Clic en el objetivo
    if jugando and target.distance(x, y) < 25:
        score += 1
        actualizar_texto()
        mover_objetivo()

def loop_juego():
    """Bucle principal no bloqueante"""
    global jugando
    if not jugando:
        return

    # Si se acaba el tiempo
    if time.time() - inicio >= duracion:
        detener_juego()
        return

    mover_objetivo()
    wn.update()
    wn.ontimer(loop_juego, 800)

def detener_juego():
    """Finaliza el juego y muestra el puntaje"""
    global jugando
    jugando = False
    target.hideturtle()
    texto.goto(0, 0)
    texto.clear()
    texto.write(f"⏹️ Juego terminado\nPuntaje final: {score}",
                align="center", font=("Arial", 24, "bold"))
    wn.update()

# --- EVENTO DE CLIC ---
wn.onscreenclick(clic_general)

# --- INICIO ---
wn.update()
wn.mainloop()
