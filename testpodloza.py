import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective

pygame.init()

width, height = 800, 600
display = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

gluPerspective(45, (width / height), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Rysowanie prostokąta
    glBegin(GL_QUADS)
    glVertex3f(-1, -1, 0)
    glVertex3f(1, -1, 0)
    glVertex3f(1, 1, 0)
    glVertex3f(-1, 1, 0)
    glEnd()

    pygame.display.flip()
    pygame.time.wait(10)
