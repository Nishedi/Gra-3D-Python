from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
class Door:
    colors = (155, 143, 129)

    surface = (1, 5, 6, 2) # przod domu)

    edges = (
        (2, 1),
        (2, 6),
        (6, 5),
        (1,5)
    )
    size = 0
    offsetx=0
    offsety=0
    offsetz=0
    deep = 5

    def __init__(self, offsetx, offsety, offsetz):
        self.size=0.2
        self.offsetx=offsetx
        self.offsety=offsety
        self.offsetz=offsetz

    def verticlesHause(self):
        off = 0.81
        doorHeight = 0.35
        self.offsety = -0.45
        vertices = ((self.size+self.offsetx,  -self.size+self.offsety-doorHeight,    -self.size+self.offsetz+off),
            (self.size+self.offsetx,  -self.size+self.offsety-doorHeight,    self.size+self.offsetz+off),
            (-self.size+self.offsetx, -self.size+self.offsety-doorHeight,    self.size+self.offsetz+off),
            (-self.size+self.offsetx, -self.size+self.offsety-doorHeight,    -self.size+self.offsetz+off),

            (self.size+self.offsetx,     self.size+self.offsety,  -self.size+self.offsetz+off),
            (self.size+self.offsetx,     self.size+self.offsety,  self.size+self.offsetz+off),
            (-self.size+self.offsetx,    self.size+self.offsety,  self.size+self.offsetz+off),
            (-self.size+self.offsetx,    self.size+self.offsety,  -self.size+self.offsetz+off))
        
        return vertices


    def show_cube(self):
        verticles =self.verticlesHause()
        glBegin(GL_QUADS)
        for i, vertex in enumerate(self.surface):
            wsp = 20/(self.deep)
            colorx = (0.5, 0.35, 0.05)
            color2 = (colorx[0] * wsp, colorx[1] * wsp, colorx[2] * wsp)
            glColor3fv(color2)
            glVertex3fv(verticles[vertex])
        glEnd()
        return 
    
    def moveDeep(self, deep):
        self.offsetz=deep  
    def moveTest(self, incrementer):
        self.offsetz+=incrementer

    def moveWidth(self, width):
        self.offsetx=width

    