import pygame as pg
from pygame.locals import *
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from scipy.special import comb
import numpy as np
import threading
from scipy.special import binom
import random
import string
import re


width, height = 600, 600  
accuracy = 100
a = 5

p1=[[-3.0, -1.0, 1.0, 3.0],[-3.0, -3.0, -3.0, -3.0],[0, 0, 0, 0]]
p2=[[-3.0, -3.0, -3.0, -3.0],[-3.0, -1.0, 1.0, 3.0],[0, 0, 0, 0]]
p3=[[3.0, 3.0, 3.0, 3.0],[-3.0, -1.0, 1.0, 3.0],[0, 0, 0, 0]]
p4=[[-3.0, -1.0, 1.0, 3.0],[3.0, 3.0, 3.0, 3.0],[0, 0, 0, 0]]
point1=[p1[0][0],p1[1][0],p1[2][0]]
point2=[p1[0][3],p1[1][3],p1[2][3]]
point3=[p2[0][3],p2[1][3],p2[2][3]]
point4=[p3[0][3],p3[0][3],p3[2][3]]
P0u = []
P1u = []
P0w = []
P1w = []

def Q(u, w):
    du = int(100*u)
    dw = int(100*w)
    global point1, point2, point3, point4, P0u, P0w, P1u, P1w
    x = P0u[0][du]*(1-w) + P1u[0][du]*w + P0w[0][dw]*(1-u) + P1w[0][dw]*u - point1[0]*(1-u)*(1-w) - point2[0]*(1-u)*w - point3[0]*(1-w)*u - point4[0]*u*w
    y = P0u[1][du]*(1-w) + P1u[1][du]*w + P0w[1][dw]*(1-u) + P1w[1][dw]*u - point1[1]*(1-u)*(1-w) - point2[1]*(1-u)*w - point3[1]*(1-w)*u - point4[1]*u*w
    z = P0u[2][du]*(1-w) + P1u[2][du]*w + P0w[2][dw]*(1-u) + P1w[2][dw]*u - point1[2]*(1-u)*(1-w) - point2[2]*(1-u)*w - point3[2]*(1-w)*u - point4[2]*u*w
    return x, y, z
 
def bezier(P):
    n = 3
    Num_t=100
    px, py, pz = [None]*(Num_t+1),[None]*(Num_t+1),[None]*(Num_t+1)

    for j in range(Num_t+1):
        t = j / float(Num_t)
        px[j],py[j],pz[j]=0.0,0.0,0.0
        for i in range(4):
            px[j] += binom(n,i)*t**i*(1-t)**(n-i)*P[0][i]
            py[j] += binom(n,i)*t**i*(1-t)**(n-i)*P[1][i]
            pz[j] += binom(n,i)*t**i*(1-t)**(n-i)*P[2][i]

    return px, py, pz

def draw1():
    global P0u, P0w, P1u, P1w
    glPointSize(3)
    glLineWidth(3)
    glColor3f(0.53, 0.33, 0.65)
    xvals, yvals, zvals = bezier(p1)
    P0u = [xvals, yvals, zvals]
    xvals, yvals, zvals = bezier(p2)
    P0w = [xvals, yvals, zvals]
    xvals, yvals, zvals = bezier(p3)
    P1u = [xvals, yvals, zvals]
    xvals, yvals, zvals = bezier(p4)
    P1w = [xvals, yvals, zvals]

def draw2():
    global P0u, P0w, P1u, P1w
    for u1 in range(0, 101, a):
        xvals = []
        yvals = []
        zvals = []
        u = u1/100
        for w1 in range(0, 101, a):
            w = w1/100
            x, y, z = Q(u, w)
            xvals.append(x)
            yvals.append(y)
            zvals.append(z)
        glBegin(GL_LINE_STRIP)
        for i in range(len(xvals)):
            glVertex3f(xvals[i],yvals[i],zvals[i])
        glEnd()

def draw3():
    global P0u, P0w, P1u, P1w
    for w1 in range(0, 101, a):
        xvals = []
        yvals = []
        zvals = []
        w = w1/100
        for u1 in range(0, 101, a):
            u = u1/100
            x, y, z = Q(u, w)
            xvals.append(x)
            yvals.append(y)
            zvals.append(z)
        glBegin(GL_LINE_STRIP)
        for i in range(len(xvals)):
            glVertex3f(xvals[i],yvals[i],zvals[i])
        glEnd()

def draw():
    draw1()
    draw2()
    draw3()

def make_window():
    master = tk.Tk() 
    master.title("Окно управления")
    master.geometry('430x640')

    scale_1 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL) 
    label_1 = tk.Label(master, text="x1")
    scale_2 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_2 = tk.Label(master, text="y1")
    scale_3 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_3 = tk.Label(master, text="z1")
    label_1.grid(row=0, column=0) 
    scale_1.grid(row=0, column=1) 
    label_2.grid(row=0, column=2) 
    scale_2.grid(row=0, column=3)
    label_3.grid(row=0, column=4) 
    scale_3.grid(row=0, column=5)
    scale_4 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL) 
    label_4 = tk.Label(master, text="x2")
    scale_5 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_5 = tk.Label(master, text="y2")
    scale_6 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_6 = tk.Label(master, text="z2")
    label_4.grid(row=1, column=0) 
    scale_4.grid(row=1, column=1) 
    label_5.grid(row=1, column=2) 
    scale_5.grid(row=1, column=3)
    label_6.grid(row=1, column=4) 
    scale_6.grid(row=1, column=5)
    scale_7 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL) 
    label_7 = tk.Label(master, text="x3")
    scale_8 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_8 = tk.Label(master, text="y3")
    scale_9 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_9 = tk.Label(master, text="z3")
    label_7.grid(row=2, column=0) 
    scale_7.grid(row=2, column=1) 
    label_8.grid(row=2, column=2) 
    scale_8.grid(row=2, column=3)
    label_9.grid(row=2, column=4) 
    scale_9.grid(row=2, column=5)
    scale_10 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL) 
    label_10 = tk.Label(master, text="x4")
    scale_11 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_11 = tk.Label(master, text="y4")
    scale_12 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_12 = tk.Label(master, text="z4")
    label_10.grid(row=3, column=0) 
    scale_10.grid(row=3, column=1) 
    label_11.grid(row=3, column=2) 
    scale_11.grid(row=3, column=3)
    label_12.grid(row=3, column=4) 
    scale_12.grid(row=3, column=5)
    scale_13 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL) 
    label_13 = tk.Label(master, text="x5")
    scale_14 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_14 = tk.Label(master, text="y5")
    scale_15 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_15 = tk.Label(master, text="z5")
    label_13.grid(row=4, column=0) 
    scale_13.grid(row=4, column=1) 
    label_14.grid(row=4, column=2) 
    scale_14.grid(row=4, column=3)
    label_15.grid(row=4, column=4) 
    scale_15.grid(row=4, column=5)
    scale_16 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL) 
    label_16 = tk.Label(master, text="x6")
    scale_17 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_17 = tk.Label(master, text="y6")
    scale_18 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_18 = tk.Label(master, text="z6")
    label_16.grid(row=5, column=0) 
    scale_16.grid(row=5, column=1) 
    label_17.grid(row=5, column=2) 
    scale_17.grid(row=5, column=3)
    label_18.grid(row=5, column=4) 
    scale_18.grid(row=5, column=5)
    scale_19 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL) 
    label_19 = tk.Label(master, text="x7")
    scale_20 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_20 = tk.Label(master, text="y7")
    scale_21 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_21 = tk.Label(master, text="z7")
    label_19.grid(row=6, column=0) 
    scale_19.grid(row=6, column=1) 
    label_20.grid(row=6, column=2) 
    scale_20.grid(row=6, column=3)
    label_21.grid(row=6, column=4) 
    scale_21.grid(row=6, column=5)
    scale_22 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL) 
    label_22 = tk.Label(master, text="x8")
    scale_23 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_23 = tk.Label(master, text="y8")
    scale_24 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_24 = tk.Label(master, text="z8")
    label_22.grid(row=7, column=0) 
    scale_22.grid(row=7, column=1) 
    label_23.grid(row=7, column=2) 
    scale_23.grid(row=7, column=3)
    label_24.grid(row=7, column=4) 
    scale_24.grid(row=7, column=5)
    scale_25 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL) 
    label_25 = tk.Label(master, text="x9")
    scale_26 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_26 = tk.Label(master, text="y9")
    scale_27 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_27 = tk.Label(master, text="z9")
    label_25.grid(row=8, column=0) 
    scale_25.grid(row=8, column=1) 
    label_26.grid(row=8, column=2) 
    scale_26.grid(row=8, column=3)
    label_27.grid(row=8, column=4) 
    scale_27.grid(row=8, column=5)
    scale_28 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL) 
    label_28 = tk.Label(master, text="x10")
    scale_29 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_29 = tk.Label(master, text="y10")
    scale_30 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_30 = tk.Label(master, text="z10")
    label_28.grid(row=9, column=0) 
    scale_28.grid(row=9, column=1) 
    label_29.grid(row=9, column=2) 
    scale_29.grid(row=9, column=3)
    label_30.grid(row=9, column=4) 
    scale_30.grid(row=9, column=5)
    scale_31 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL) 
    label_31 = tk.Label(master, text="x11")
    scale_32 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_32 = tk.Label(master, text="y11")
    scale_33 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_33 = tk.Label(master, text="z11")
    label_31.grid(row=10, column=0) 
    scale_31.grid(row=10, column=1) 
    label_32.grid(row=10, column=2) 
    scale_32.grid(row=10, column=3)
    label_33.grid(row=10, column=4) 
    scale_33.grid(row=10, column=5)
    scale_34 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL) 
    label_34 = tk.Label(master, text="x12")
    scale_35 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_35 = tk.Label(master, text="y12")
    scale_36 = Scale(master, from_=-1, to=1,resolution=0.1, orient=HORIZONTAL)
    label_36 = tk.Label(master, text="z12")
    label_34.grid(row=11, column=0) 
    scale_34.grid(row=11, column=1) 
    label_35.grid(row=11, column=2) 
    scale_35.grid(row=11, column=3)
    label_36.grid(row=11, column=4) 
    scale_36.grid(row=11, column=5)

    def ButtonCall():
        global p1, p2, p3, p4, point1, point2, point3, point4
        #a1
        p1[0][0]+=float(scale_1.get())
        p1[1][0]+=float(scale_2.get())
        p1[2][0]+=float(scale_3.get())
        #a2
        p1[0][1]+=float(scale_4.get())
        p1[1][1]+=float(scale_5.get())
        p1[2][1]+=float(scale_6.get())
        #a3
        p1[0][2]+=float(scale_7.get())
        p1[1][2]+=float(scale_8.get())
        p1[2][2]+=float(scale_9.get())
        #a4
        p1[0][3]+=float(scale_10.get())
        p1[1][3]+=float(scale_11.get())
        p1[2][3]+=float(scale_12.get())
        #a12
        p2[0][0]+=float(scale_1.get())
        p2[1][0]+=float(scale_2.get())
        p2[2][0]+=float(scale_3.get())
        #a5
        p2[0][1]+=float(scale_13.get())
        p2[1][1]+=float(scale_14.get())
        p2[2][1]+=float(scale_15.get())
        #a6
        p2[0][2]+=float(scale_16.get())
        p2[1][2]+=float(scale_17.get())
        p2[2][2]+=float(scale_18.get())
        #a7
        p2[0][3]+=float(scale_19.get())
        p2[1][3]+=float(scale_20.get())
        p2[2][3]+=float(scale_21.get())
        #a41
        p3[0][0]+=float(scale_10.get())
        p3[1][0]+=float(scale_11.get())
        p3[2][0]+=float(scale_12.get())
        #a8
        p3[0][1]+=float(scale_22.get())
        p3[1][1]+=float(scale_23.get())
        p3[2][1]+=float(scale_24.get())
        #a9
        p3[0][2]+=float(scale_25.get())
        p3[1][2]+=float(scale_26.get())
        p3[2][2]+=float(scale_27.get())
        #a10
        p3[0][3]+=float(scale_28.get())
        p3[1][3]+=float(scale_29.get())
        p3[2][3]+=float(scale_30.get())
        #a71
        p4[0][0]+=float(scale_19.get())
        p4[1][0]+=float(scale_20.get())
        p4[2][0]+=float(scale_21.get())
        #a101
        p4[0][3]+=float(scale_28.get())
        p4[1][3]+=float(scale_29.get())
        p4[2][3]+=float(scale_30.get())
        #a11
        p4[0][1]+=float(scale_31.get())
        p4[1][1]+=float(scale_32.get())
        p4[2][1]+=float(scale_33.get())
        #a12
        p4[0][2]+=float(scale_34.get())
        p4[1][2]+=float(scale_35.get())
        p4[2][2]+=float(scale_36.get())
        point1=[p1[0][0],p1[1][0],p1[2][0]]
        point2=[p1[0][3],p1[1][3],p1[2][3]]
        point3=[p2[0][3],p2[1][3],p2[2][3]]
        point4=[p3[0][3],p3[0][3],p3[2][3]]

    button1 = tk.Button(master, text="Изменить значения", command=ButtonCall)
    button1.grid(row=12, column=3)

    spinbox_1 = tk.Spinbox(master, values = [5, 10, 20, 25, 50]) 
    label_a = tk.Label(master, text="Шаг")
    spinbox_1.grid(row=13, column=3) 
    label_a.grid(row=13, column=2)

    def Buttonacc():
        global a
        a = int(spinbox_1.get())

    button2 = tk.Button(master, text="Изменить шаг", command=Buttonacc)
    button2.grid(row=14, column=3)

    def generate_random_string(length):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

    def save_file():
        a = generate_random_string(4)
        print(a)
        my_file = open(a + ".txt", "w+")
        my_file.write(str(p1[0][0]) + " " + str(p1[1][0]) + " " + str(p1[2][0]) + "\n")
        my_file.write(str(p1[0][1]) + " " + str(p1[1][1]) + " " + str(p1[2][1]) + "\n")
        my_file.write(str(p1[0][2]) + " " + str(p1[1][2]) + " " + str(p1[2][2]) + "\n")
        my_file.write(str(p1[0][3]) + " " + str(p1[1][3]) + " " + str(p1[2][3]) + "\n")
        my_file.write(str(p2[0][1]) + " " + str(p2[1][1]) + " " + str(p2[2][1]) + "\n")
        my_file.write(str(p2[0][2]) + " " + str(p2[1][2]) + " " + str(p2[2][2]) + "\n")
        my_file.write(str(p2[0][3]) + " " + str(p2[1][3]) + " " + str(p2[2][3]) + "\n")
        my_file.write(str(p3[0][1]) + " " + str(p3[1][1]) + " " + str(p3[2][1]) + "\n")
        my_file.write(str(p3[0][2]) + " " + str(p3[1][2]) + " " + str(p3[2][2]) + "\n")
        my_file.write(str(p3[0][3]) + " " + str(p3[1][3]) + " " + str(p3[2][3]) + "\n")
        my_file.write(str(p4[0][1]) + " " + str(p4[1][1]) + " " + str(p4[2][1]) + "\n")
        my_file.write(str(p4[0][2]) + " " + str(p4[1][2]) + " " + str(p4[2][2]) + "\n")
        my_file.close()

    button2 = tk.Button(master, text="Сохранить", command=save_file)
    button2.grid(row=15, column=3)

    def select_file():
        global p1, p2, p3, p4, point1, point2, point3, point4
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        my_file = open(filename, "r+")
        data =[]
        for line in my_file:
            data.append([float(x) for x in line.split()])
        p1 = [[data[0][0],data[1][0],data[2][0],data[3][0]],[data[0][1],data[1][1],data[2][1],data[3][1]],[data[0][2],data[1][2],data[2][2],data[3][2]]]
        p2 = [[data[0][0],data[4][0],data[5][0],data[6][0]],[data[0][1],data[4][1],data[5][1],data[6][1]],[data[0][2],data[4][2],data[5][2],data[6][2]]]
        p3 = [[data[3][0],data[7][0],data[8][0],data[9][0]],[data[3][1],data[7][1],data[8][1],data[9][1]],[data[3][2],data[7][2],data[8][2],data[9][2]]]
        p4 = [[data[6][0],data[10][0],data[11][0],data[9][0]],[data[6][1],data[10][1],data[11][1],data[9][1]],[data[6][2],data[10][2],data[11][2],data[9][2]]]
        point1=[p1[0][0],p1[1][0],p1[2][0]]
        point2=[p1[0][3],p1[1][3],p1[2][3]]
        point3=[p2[0][3],p2[1][3],p2[2][3]]
        point4=[p3[0][3],p3[0][3],p3[2][3]]

        my_file.close()

    
    button3 = tk.Button(master, text="Загрузить", command=select_file)
    button3.grid(row=16, column=3)

    tk.mainloop()

def main():
    t1 = threading.Thread(target=make_window)
    t1.start()

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

        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)

        draw()
        
        pg.display.flip()
        pg.time.wait(30)

if __name__ == "__main__":
    main()