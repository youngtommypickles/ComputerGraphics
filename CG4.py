#М8О-301Б-19
#Цыкин Иван
#Вариант 14
#Эллиптический цилиндр
from OpenGL.GLUT import * #Подключение библиотек
from OpenGL.GL import *
from OpenGL.GLU import *
import math


col1 = 0.27
col2 = 0.73
col3 = 0.62

xrot = 0.2
yrot = 0.0

d1 = 1
d2 = 1
a = 0.5
b = 0.5
c = 0.5   

def init():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClearColor(0.5, 0.5, 0.5, 0) # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Определяем границы рисования по горизонтали и вертикали
    glEnable ( GL_DEPTH_TEST ) #установка параметров заливки
    glDepthMask ( GL_TRUE )
    glDepthFunc ( GL_LEQUAL )
    glFlush()
    
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

def display(): #функция вывоа на экран
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    global xrot, yrot, zrot, lightpos
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    gluLookAt(0.0, 0.0, 10.0,0.0, 0.0, 0.0,0.0, 1.0, 0.0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 1, 0))
    glPointSize(1)
    glLineWidth(1)
    glColor3f(col1, col2, col3)
    draw_cylinder(d1, a, b, c)
    glPointSize(3)
    glLineWidth(3)
    glColor3f(0, 0, 0)
    draw_cylinder2(d1, a, b, c)
    glutSwapBuffers()

def specialkeys(key, x, y): #работа с клавиатурой
    global xrot
    global yrot
    global a
    global b 
    global c 
    global d1
    global col1
    global col2
    global col3
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP: xrot -= 2.0             # Уменьшаем угол вращения по оси X
    if key == GLUT_KEY_DOWN: xrot += 2.0             # Увеличиваем угол вращения по оси X
    if key == GLUT_KEY_LEFT:  yrot -= 2.0             # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:  yrot += 2.0             # Увеличиваем угол вращения по оси Y
    if key == GLUT_KEY_F1:
        if a<3: a += 0.3
        else: a = 0.5             
    if key == GLUT_KEY_F2:
        if b<3: b += 0.3
        else: b = 0.5          
    if key == GLUT_KEY_F3:
        if c<6: c += 0.3
        else: c = 0.5           
    if key == GLUT_KEY_F4:
        if d1<128: d1*=2
        else: d1 = 1
    if key == GLUT_KEY_F5:
        if col1 > 1: col1= 0.05
        else: col1 += 0.05          
    if key == GLUT_KEY_F6:
        if col2 > 1: col2 = 0.05
        else: col2 += 0.05           
    if key == GLUT_KEY_F7:
        if col3 > 1: col3 = 0.05
        else: col3 += 0.05             
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
glutInitWindowSize(800, 800)
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
glutCreateWindow("LAB 4-5 Tsykin Ivan")
glutReshapeFunc(resize)
glutDisplayFunc(display)
glutSpecialFunc(specialkeys)
init()
glutMainLoop()