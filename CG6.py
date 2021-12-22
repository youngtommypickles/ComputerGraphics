#М8О-301Б-19
#Цыкин Иван
#Вариант 14
#Эллиптический цилиндр
import pygame as pg
from pygame.locals import *
import tkinter as tk
from tkinter import *

from OpenGL.GL import *
from OpenGL.GLU import *
import math
import threading 

import time

col1 = 1
col2 = 1
col3 = 1

d1 = 1
a = 0.5
b = 0.5
c = 0.50

phi1 = 0
phi2 = 0
phi3 = 0

def draw_cylinder(uistacks, fA, fB, fC):
    sstep = math.pi/uistacks
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_POLYGON_BIT)
    for i in range(2*uistacks+1):
        t = sstep*i
        glVertex3f(fA*math.cos(t), fB*math.sin(t), fC/2)
        glVertex3f(fA*math.cos(t), fB*math.sin(t), -fC/2)
    glEnd()

    glBegin(GL_POLYGON)
    for i in range(2*uistacks+1):
        t = sstep*i
        glVertex3f(fA*math.cos(t), fB*math.sin(t), fC/2)
    glEnd()

    glBegin(GL_POLYGON)
    for i in range(2*uistacks+1):
        t = sstep*i
        glVertex3f(fA*math.cos(t), fB*math.sin(t), -fC/2)
    glEnd()

def draw_cylinder2(uistacks, fA, fB, fC):
    sstep = math.pi/uistacks
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_POLYGON_BIT)
    for i in range(2*uistacks+1):
        t = sstep*i
        glVertex3f(fA*math.cos(t), fB*math.sin(t), fC/2)
        glVertex3f(fA*math.cos(t), fB*math.sin(t), -fC/2)
    glEnd()

def draw():
	glPointSize(1)
	glLineWidth(1)
	draw_cylinder(d1, a, b, c)
	glPointSize(3)
	glLineWidth(3)
	glColor3f(0, 0, 0)
	draw_cylinder2(d1, a, b, c)

def make_window():
	window = tk.Tk()
	window.title("Окно управления")
	window.geometry('280x200')

	scale_accuracy1 = tk.Scale(window, from_=0, to=180, orient=HORIZONTAL, length=200)
	label_accuracy1 = tk.Label(window, text="R: phi1")
	label_accuracy1.grid(row=1, column=0)
	scale_accuracy1.grid(row=1, column=1)

	scale_accuracy2 = tk.Scale(window, from_=0, to=180, orient=HORIZONTAL, length=200)
	label_accuracy2 = tk.Label(window, text="G: phi2")
	label_accuracy2.grid(row=2, column=0)
	scale_accuracy2.grid(row=2, column=1)

	scale_accuracy3 = tk.Scale(window, from_=0, to=180, orient=HORIZONTAL, length=200)
	label_accuracy3 = tk.Label(window, text="B: phi3")
	label_accuracy3.grid(row=3, column=0)
	scale_accuracy3.grid(row=3, column=1)

	def ButtonCall():
		global phi1, phi2, phi3
		phi1 = scale_accuracy1.get() * math.pi/180
		phi2 = scale_accuracy2.get() * math.pi/180
		phi3 = scale_accuracy3.get() * math.pi/180

	label_accuracy4 = tk.Label(window, text="Цвет изменяется по закону: SIN(t+phi)")
	label_accuracy4.grid(row=5, column=1)

	button = tk.Button(window, text="Click", command=ButtonCall)
	button.grid(row=7, column=1)

	tk.mainloop()

def main():

	t1 = threading.Thread(target=make_window)
	t1.start()

	global a, b, c, d1, col1, col2, col3, t
	pg.init()
	display = (600, 600)
	screen = pg.display.set_mode(display, DOUBLEBUF|OPENGL)
	pg.display.set_caption('Цыкин Иван')

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(0.0, 0.0, -5)
	glClearColor(200/255, 200/255, 200/255, 1)

	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				quit()
			if event.type == pg.MOUSEMOTION:
				pressed = pg.mouse.get_pressed(3)
				if pressed[0]:
					glRotatef(2, event.rel[1], event.rel[0], 0)
			if event.type == pg.MOUSEBUTTONDOWN:
				if event.button == 4:
					glScalef(1.1, 1.1, 1.1)
				elif event.button == 5:
					glScalef(0.9, 0.9, 0.9)
                    
			pressed = pg.key.get_pressed() #считывание команд с клавиатуры
			if pressed[pg.K_F1]:
				if a<2.5: a += 0.3
				else: a = 0.5
			if pressed[pg.K_F2]:
				if b < 2.5: b += 0.3
				else: b = 0.5
			if pressed[pg.K_F3]:  
				if c<6: c += 0.3
				else: c = 0.5
			if pressed[pg.K_F4]:
				if d1<128: d1*=2
				else: d1 = 1

		t = time.time()
		glColor3f(col1*abs(math.sin(t+phi1)), col2*abs(math.sin(t+phi2)), col3*abs(math.sin(t+phi3)))
		glClearColor(1, 1, 1, 1)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glEnable(GL_DEPTH_TEST)

		draw()
        
		pg.display.flip()
		pg.time.wait(30)

if __name__ == "__main__":
    main()