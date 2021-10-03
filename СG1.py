from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

window = 0                                            
width, height = 600, 400                               
mas1 = dict(X=[], Y=[])
a = 1
n = 2

def init():
    glClearColor(1, 1, 1, 1.0)                # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)                # Определяем границы рисования по горизонтали и вертикали

def specialkeys(key, x, y):                # Обработчики для клавиш со стрелками
	global n 
	global a
	if key == GLUT_KEY_UP and n < 1024: n*=2
	if key == GLUT_KEY_DOWN and n > 2: n/=2           
	if key == GLUT_KEY_LEFT and a > 1: a-=1
	if key == GLUT_KEY_RIGHT and a < 10: a+=1
	glutPostRedisplay()

def Draw_OS(alpha, d):
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

def f1(x, a): 
	y = -1 * ((-2 * x * x - a * a + (8 * a * a * x * x + a**4 )**(0.5))/2)**(0.5)
	return y

def f2(x, a): 
	y = ((-2 * x * x - a * a + (8 * a * a * x * x + a**4 )**(0.5))/2)**(0.5)
	return y

def Init(start, finish, n, a):
	x = start
	dx = (finish - start)/(n)
	while x >= start and x <= finish:
		mas1['X'].append(x/10)
		mas1['Y'].append(f1(x, a)/10)
		x+=dx
	x = finish
	while x >= start and x <= finish:
		mas1['X'].append(x/10)
		mas1['Y'].append(f2(x, a)/10) 
		x-=dx

def Draw_func(start, finish, n, a):
	glLoadIdentity()
	Init(start, finish, n, a)
	glPointSize(3)
	glLineWidth(3)
	glColor3f(1, 0, 0)
	glBegin(GL_LINE_STRIP)
	for i in range(0, len(mas1['X']), 1):
		glVertex2f(mas1['X'][i], mas1['Y'][i])
	mas1['X'].clear()
	mas1['Y'].clear()
	glEnd()

def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glPushMatrix()
	Draw_OS(0, 0.02)
	Draw_OS(90, 0.02)
	Draw_func(-a, a, n, a)
	glPopMatrix()
	glutSwapBuffers()             

glutInit(sys.argv)                                          
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(width, height)                      
glutInitWindowPosition(50, 50)                          
window = glutCreateWindow("KG1") 
glutDisplayFunc(draw)
glutSpecialFunc(specialkeys)
init()
glutMainLoop()