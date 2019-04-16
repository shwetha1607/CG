import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def Square():
    glBegin(GL_POINTS)
    glPointSize(10.0)
    glColor3f(1,1,0)
    glVertex2f(100,100)
    glVertex2f(100,200)
    glEnd()
    glFlush()
    


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 100.0, 500.0)
    
    glTranslatef(0.0,0.0, -5)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Square()
        pygame.display.flip()
        pygame.time.wait(10)
    
    
main()
