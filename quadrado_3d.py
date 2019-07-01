import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

#monta o quadrado
verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

arestas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

superfices =(
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),    
    )
cores = (
    #color red 1.00 green 0.43 blue 0.78
    (1.00, 0.43,0.78),
    (0.43,1.00,0.78),
    (0.43,0.78,1.00),
    (1.00,1.00,1.00),
    (0.43,0.430,0.43),
    (1.00,0.43,0.43),
    (1.00, 0.43,0.78),
    (0.43,1.00,0.78),
    (0.43,0.78,1.00),
    (1.00,1.00,1.00),
    (0.43,0.430,0.43),
    (1.00,0.43,0.43),
 
    )

def Cube():
    glBegin(GL_QUADS)
    
    for superfice in superfices:
       y = 0
       for vertex in superfice:
           y+=1
           glColor3fv(cores[y])
           glVertex3fv(verticies[vertex])
    glEnd()

    
    glBegin(GL_LINES)
    for aresta in arestas:
        for vertex in aresta:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(0.560784, 0.560784, 0.737255, 0)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
