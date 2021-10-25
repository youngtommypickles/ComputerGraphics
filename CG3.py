#М8О-301Б-19
#Цыкин Иван
#Вариант 5
#Эллипсойд
from OpenGL.GLUT import * #Подключение библиотек
from OpenGL.GL import *
from OpenGL.GLU import *
import math

#константы
ngon=60
angle_step=2*math.pi/ngon
r1_step = 0.005
r2_step = 0.001
delta=0.6
theta1 = 2*math.pi/ngon

xrot = 0.2
yrot = 0.0

d1 = 1
d2 = 1
a = 0.5
b = 0.5
c = 0.5   

def init():
    glClearColor(0.9, 0.9, 0.9, 1.0) # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Определяем границы рисования по горизонтали и вертикали
    glEnable ( GL_DEPTH_TEST ) #установка параметров заливки
    glDepthMask ( GL_TRUE )
    glDepthFunc ( GL_LEQUAL )

def Draw(uistacks, uislices, fA, fB, fC): #функция рисует фигуру
    tstep = math.pi/uislices
    sstep = math.pi/uistacks
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    for i in range(2*uislices):
        t = tstep*i
        glBegin(GL_POLYGON_BIT)
        for j in range(uistacks+1):
            s = sstep*j
            glVertex3f(fA * math.cos(t) * math.cos(s), fB * math.cos(t) * math.sin(s), fC * math.sin(t))
            glVertex3f(fA * math.cos(t+tstep) * math.cos(s), fB *math.cos(t+tstep) * math.sin(s), fC * math.sin(t+tstep))
        glEnd()

def Draw2(uistacks, uislices, fA, fB, fC): #функция рисует границы
    tstep = math.pi/uislices
    sstep = math.pi/uistacks
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    for i in range(2*uislices):
        t = tstep*i
        glBegin(GL_POLYGON_BIT)
        for j in range(uistacks+1):
            s = sstep*j
            glVertex3f(fA * math.cos(t) * math.cos(s), fB * math.cos(t) * math.sin(s), fC * math.sin(t))
            glVertex3f(fA * math.cos(t+tstep) * math.cos(s), fB *math.cos(t+tstep) * math.sin(s), fC * math.sin(t+tstep))
        glEnd()

def display(): #функция вывоа на экран
    global xrot, yrot, zrot
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 10.0,0.0, 0.0, 0.0,0.0, 1.0, 0.0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glPointSize(1)
    glLineWidth(1)
    glColor3f(0.37, 0.83, 0.61)
    Draw(d1, d2, a, b, c)
    glPointSize(3)
    glLineWidth(3)
    glColor3f(0.0, 0.0, 0.0)
    Draw2(d1, d2, a, b, c)
    glFlush()
    glutSwapBuffers()

def specialkeys(key, x, y): #работа с клавиатурой
    global xrot
    global yrot
    global a
    global b 
    global c 
    global d1 
    global d2
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP: xrot -= 2.0             # Уменьшаем угол вращения по оси X
    if key == GLUT_KEY_DOWN: xrot += 2.0             # Увеличиваем угол вращения по оси X
    if key == GLUT_KEY_LEFT:  yrot -= 2.0             # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:  yrot += 2.0             # Увеличиваем угол вращения по оси Y
    if key == GLUT_KEY_F1:
        if a<3.5: a += 0.3
        else: a = 0.5             
    if key == GLUT_KEY_F2:
        if b<3.5: b += 0.3
        else: b = 0.5          
    if key == GLUT_KEY_F3:
        if c<3.5: c += 0.3
        else: c = 0.5           
    if key == GLUT_KEY_F4:
        if d1<128: d1*=2
        else: d1 = 1             
    if key == GLUT_KEY_F5:
        if d2<128: d2*=2
        else: d2 = 1  
    glutPostRedisplay()    

def resize(*args): #функция масштабирования
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, args[0], args[1])
    gluPerspective(45.0, 1.0 * args[0] / args[0], 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

#main
glutInit(sys.argv)
glutInitWindowPosition(50, 50)
glutInitWindowSize(1200, 800)
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
glutCreateWindow("CG3")
glutDisplayFunc(display)
glutReshapeFunc(resize)
glutSpecialFunc(specialkeys)
init()
glutMainLoop()