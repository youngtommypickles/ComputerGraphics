#М8О-301Б-19
#Цыкин Иван
#Вариант 2
#Октайдер
import pygame as pg #подключение нужных библиотек
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

global xrot #ротация по х
global yrot #ротация по у

xrot = 0.0 
yrot = 0.0

verticles = ( #вершины
    (0, 0, 1),
    (-1, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 0, -1)
    )

edges = ( #края
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (5, 1),
    (5, 2),
    (5, 3),
    (5, 4),
    (2, 1),
    (2, 3),
    (4, 1),
    (4, 3)
    )

triple = ( #треугольники
    (0, 1, 2),
    (0, 2, 3),
    (0, 3, 4),
    (0, 4, 1),
    (5, 1, 2),
    (5, 2, 3), 
    (5, 3, 4),
    (5, 4, 1)
    )

def octahedron(): #функция рисования 
    glColor3f(0, 0, 0)
    glPointSize(3)
    glLineWidth(3)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticles[vertex])
    glEnd()
    glColor3f(1, 1, 1)
    glPointSize(1)
    glLineWidth(1)
    glBegin(GL_TRIANGLES)
    for tr in triple:
        for vertex in tr:
            glVertex3fv(verticles[vertex])
    glEnd()


def main(): #главная функция
    global xrot
    global yrot
    global a

    pg.init() #инициализайия
    display = (1280, 800)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0) #перспектив

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            pressed = pg.key.get_pressed() #считывание команд с клавиатуры
            if pressed[pg.K_UP]:
                xrot-=0.5
            if pressed[pg.K_DOWN]:
                xrot+=0.5
            if pressed[pg.K_LEFT]:  
                yrot-=0.5
            if pressed[pg.K_RIGHT]:
                yrot+=0.5 

        glClearColor(1.0, 1.0, 1.0, 1.0)                # белый цвет для первоначальной закраски
        glRotatef(xrot, 1.0, 0.0, 0.0)
        glRotatef(yrot, 0.0, 1.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        octahedron()
        pg.display.flip()
        pg.time.wait(10)

main()
