import tkinter as tk
from tkinter import *
from OpenGL.GL import * #импортирование библиотек
from OpenGL.GLUT import *
from OpenGL.GLU import *
import threading   

width, height = 600, 600  
accuracy = 100                           

Point = [1, 1, 2, 3, 3, 1]
r1 = [0, 0]
r2 = [4, 0]
fPolynomx = [0, 0, 0, 0]
sPolynomx = [0, 0, 0, 0]
fPolynomy = [0, 0, 0, 0]
sPolynomy = [0, 0, 0, 0]

def make_window():
	window = tk.Tk()
	window.title("Окно управления")
	window.geometry('250x500')

	scale_accuracy1 = tk.Scale(window, from_=-10, to=10, orient=HORIZONTAL, length=200)
	label_accuracy1 = tk.Label(window, text="x1")
	label_accuracy1.grid(row=1, column=0)
	scale_accuracy1.grid(row=1, column=1)

	scale_accuracy2 = tk.Scale(window, from_=-10, to=10, orient=HORIZONTAL, length=200)
	label_accuracy2 = tk.Label(window, text="y1")
	label_accuracy2.grid(row=2, column=0)
	scale_accuracy2.grid(row=2, column=1)

	scale_accuracy3 = tk.Scale(window, from_=-10, to=10, orient=HORIZONTAL, length=200)
	label_accuracy3 = tk.Label(window, text="x2")
	label_accuracy3.grid(row=3, column=0)
	scale_accuracy3.grid(row=3, column=1)

	scale_accuracy4 = tk.Scale(window, from_=-10, to=10, orient=HORIZONTAL, length=200)
	label_accuracy4 = tk.Label(window, text="y2")
	label_accuracy4.grid(row=4, column=0)
	scale_accuracy4.grid(row=4, column=1)

	scale_accuracy5 = tk.Scale(window, from_=-10, to=10, orient=HORIZONTAL, length=200)
	label_accuracy5 = tk.Label(window, text="x3")
	label_accuracy5.grid(row=5, column=0)
	scale_accuracy5.grid(row=5, column=1)

	scale_accuracy6 = tk.Scale(window, from_=-10, to=10, orient=HORIZONTAL, length=200)
	label_accuracy6 = tk.Label(window, text="y3")
	label_accuracy6.grid(row=6, column=0)
	scale_accuracy6.grid(row=6, column=1)

	scale_accuracy7 = tk.Scale(window, from_=-10, to=10, orient=HORIZONTAL, length=200)
	label_accuracy7 = tk.Label(window, text="rx1")
	label_accuracy7.grid(row=7, column=0)
	scale_accuracy7.grid(row=7, column=1)

	scale_accuracy8 = tk.Scale(window, from_=-10, to=10, orient=HORIZONTAL, length=200)
	label_accuracy8 = tk.Label(window, text="ry1")
	label_accuracy8.grid(row=8, column=0)
	scale_accuracy8.grid(row=8, column=1)

	scale_accuracy9 = tk.Scale(window, from_=-10, to=10, orient=HORIZONTAL, length=200)
	label_accuracy9 = tk.Label(window, text="rx2")
	label_accuracy9.grid(row=9, column=0)
	scale_accuracy9.grid(row=9, column=1)

	scale_accuracy10 = tk.Scale(window, from_=-10, to=10, orient=HORIZONTAL, length=200)
	label_accuracy10 = tk.Label(window, text="ry2")
	label_accuracy10.grid(row=10, column=0)
	scale_accuracy10.grid(row=10, column=1)

	scale_accuracy11 = tk.Scale(window, from_=2, to=100, orient=HORIZONTAL, length=200)
	label_accuracy11 = tk.Label(window, text="acc")
	label_accuracy11.grid(row=11, column=0)
	scale_accuracy11.grid(row=11, column=1)

	def ButtonCall():
		global Point, r1, r2, accuracy
		Point[0] = scale_accuracy1.get()
		Point[1] = scale_accuracy2.get()
		Point[2] = scale_accuracy3.get()
		Point[3] = scale_accuracy4.get()
		Point[4] = scale_accuracy5.get()
		Point[5] = scale_accuracy6.get()
		r1[0] = scale_accuracy7.get()
		r1[1] = scale_accuracy8.get()
		r2[0] = scale_accuracy9.get()
		r2[1] = scale_accuracy10.get()
		accuracy = scale_accuracy11.get()

	button = tk.Button(window, text="Click", command=ButtonCall)
	button.grid(row=12, column=1)

	tk.mainloop()

def calculatePolynomx():
    global Point, r1, r2, fPolynomx, sPolynomx
    fPolynomx[3] = Point[0]/10
    sPolynomx[3] = Point[2]/10
    fPolynomx[2] = r1[0]/10

    n = -1 * fPolynomx[2]
    h = sPolynomx[3]-fPolynomx[3]-fPolynomx[2]
    q = Point[4]/10 - sPolynomx[3]
    z = r2[0]/10
    x = 3*q + 2*n - z

    fPolynomx[0] = (x-5*h)/4
    fPolynomx[1] = (9*h - x)/4

    sPolynomx[1] = 3*fPolynomx[0] + fPolynomx[1]
    sPolynomx[2] = 3*fPolynomx[0] + 2*fPolynomx[1] - n
    sPolynomx[0] = q - sPolynomx[1] - sPolynomx[2]

def calculatePolynomy():
    global Point, r1, r2, fPolynomy, sPolynomy
    fPolynomy[3] = Point[1]/10
    sPolynomy[3] = Point[3]/10
    fPolynomy[2] = r1[1]/10

    n = -1 * fPolynomy[2]
    h = sPolynomy[3]-fPolynomy[3]-fPolynomy[2]
    q = Point[5]/10 - sPolynomy[3]
    z = r2[1]/10
    x = 3*q + 2*n - z

    fPolynomy[0] = (x-5*h)/4
    fPolynomy[1] = (9*h - x)/4

    sPolynomy[1] = 3*fPolynomy[0] + fPolynomy[1]
    sPolynomy[2] = 3*fPolynomy[0] + 2*fPolynomy[1] - n
    sPolynomy[0] = q - sPolynomy[1] - sPolynomy[2]

def calculatePolynom(a, t):
    return a[0] * t * t * t + a[1] * t * t + a[2] * t + a[3]

def claculatePoint(a, t):
	return calculatePolynom(a, t)

def calculate():
    calculatePolynomx()
    calculatePolynomy()

def init():
	glClearColor(0.9, 0.9, 0.9, 1.0)                # Серый цвет для первоначальной закраски
	gluOrtho2D(-1.0, 1.0, -1.0, 1.0)                # Определяем границы рисования по горизонтали и вертикали

def Draw_OS(alpha, d): #функция для рисования оси
	glLineWidth(1)
	glColor3f(0, 0, 0)
	glRotatef(alpha, 0, 0, 1)
	glBegin(GL_LINES)
	glVertex2f(-1, 0)
	glVertex2f(1, 0)
	glVertex2f(1, 0)
	glVertex2f(1-d, 0+d)
	glVertex2f(1, 0)
	glVertex2f(1-d, 0-d)
	glEnd()

def drawBegin():
	glLineWidth(1)
	glColor3f(0, 1, 0)
	glBegin(GL_LINES)
	glVertex2f(Point[0]/10, Point[1]/10)
	glVertex2f(r1[0]/10, r1[1]/10)
	glEnd()
	glColor3f(0, 0, 1)
	glBegin(GL_LINES)
	glVertex2f(Point[4]/10, Point[5]/10)
	glVertex2f(r2[0]/10, r2[1]/10)
	glEnd()
	glColor3f(0, 0, 0)
	glLineWidth(2)
	glBegin(GL_LINES)
	glVertex2f(Point[0]/10-0.05/10, Point[1]/10)
	glVertex2f(Point[0]/10+0.05/10, Point[1]/10)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(Point[2]/10-0.05/10, Point[3]/10)
	glVertex2f(Point[2]/10+0.05/10, Point[3]/10)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(Point[4]/10-0.05/10, Point[5]/10)
	glVertex2f(Point[4]/10+0.05/10, Point[5]/10)
	glEnd()

def drawPolinom():
	glRotate(270, 0,0, 1)
	global accuracy
	calculate()
	glRotate(0, 0,0, 1)
	glLineWidth(2)
	glColor3f(1, 0, 0)
	glBegin(GL_LINES)
	x = Point[0]/10
	y = Point[1]/10
	step = 1/accuracy
	i = 1/accuracy
	while i < 1:
		glVertex2f(x, y)
		x = claculatePoint(fPolynomx, i)
		y = claculatePoint(fPolynomy, i)  
		glVertex2f(x, y)
		i+=step
	glVertex2f(x, y)
	glVertex2f(Point[2]/10, Point[3]/10)
	glEnd()
	glBegin(GL_LINES)
	x = Point[2]/10
	y = Point[3]/10
	step = 1/accuracy
	i = 1/accuracy
	while i < 1:
		glVertex2f(x, y)
		x = claculatePoint(sPolynomx, i)
		y = claculatePoint(sPolynomy, i)
		glVertex2f(x, y)
		i+=step
	glVertex2f(x, y)
	glVertex2f(Point[4]/10, Point[5]/10)
	glEnd()

def draw(): #самый главный блок рисования
	glClear(GL_COLOR_BUFFER_BIT)
	glPushMatrix()
	Draw_OS(0, 0.02)
	Draw_OS(90, 0.02)
	drawPolinom()
	drawBegin()
	glPopMatrix()
	glutSwapBuffers()          

def main():
	t1 = threading.Thread(target=make_window)
	t1.start()

	glutInit() #инициализация                                         
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutInitWindowSize(width, height)                      
	glutInitWindowPosition(50, 50)                          
	window = glutCreateWindow("KG1") 
	glutDisplayFunc(draw)
	init()
	glutMainLoop()

if __name__ == "__main__":
    main()