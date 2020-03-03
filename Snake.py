import turtle
import time
import random

posponer = 0.1

#config de la ventana(wn)
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width = 600, height= 600)
wn.tracer(0)

#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#segmentos
segmentos = []

#funciones
def arriba():
	cabeza.direction = "up"
def abajo():
	cabeza.direction = "down"
def der():
	cabeza.direction = "right"
def izq():
	cabeza.direction = "left"
def mov():
	if cabeza.direction == "up":
		y = cabeza.ycor()
		cabeza.sety(y+20)
	if cabeza.direction == "down":
		y = cabeza.ycor()
		cabeza.sety(y-20)
	if cabeza.direction == "right":
		x = cabeza.xcor()
		cabeza.setx(x+20)
	if cabeza.direction == "left":
		x = cabeza.xcor()
		cabeza.setx(x-20)

#teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(der, "Right")
wn.onkeypress(izq, "Left")

while True:
	wn.update()
	#colisiones con la comida
	if cabeza.distance(comida) < 20:
		x = random.randint(-280, 280)
		y = random.randint(-280, 280)
		comida.goto(x,y)
		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.shape("square")
		nuevo_segmento.color("grey")
		nuevo_segmento.penup()
		segmentos.append(nuevo_segmento)
	#movimiento de la serpiente
	totalseg = len(segmentos)
	for i in range(totalseg -1, 0, -1):
		x = segmentos[i -1].xcor()
		y = segmentos[i -1].ycor()
		segmentos[i].goto(x,y)
	if totalseg > 0:
		x = cabeza.xcor()
		y = cabeza.ycor()
		segmentos[0].goto(x,y)



	mov()
	time.sleep(posponer)