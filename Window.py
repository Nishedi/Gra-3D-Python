from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
class Window:
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
    movementx = 0
    movementy = 0
    deep = 55

    def __init__(self, offsetx, offsety, offsetz, movementx, movementy, widthleft, widthright):
        self.size=0.2
        self.offsetx=offsetx
        self.offsety=offsety
        self.offsetz=offsetz
        self.movementx = movementx
        self.movementy = movementy
        self.widthleft=widthleft
        self.widthright=widthright

   

    def verticlesHause(self):
        off = 0.81
        self.offsety = -0.45
        widthleft = self.widthleft
        widthright = self.widthright
        movement = self.movementx
        movement2 = self.movementy
        vertices = ((self.size+self.offsetx+movement+widthleft,  -self.size+self.offsety+movement2,    -self.size+self.offsetz+off),
            (self.size+self.offsetx+movement+widthleft,  -self.size+self.offsety+movement2,    self.size+self.offsetz+off),
            (-self.size+self.offsetx+movement+widthright, -self.size+self.offsety+movement2,    self.size+self.offsetz+off),
            (-self.size+self.offsetx+movement+widthright, -self.size+self.offsety+movement2,    -self.size+self.offsetz+off),

            (self.size+self.offsetx+movement+widthleft,     self.size+self.offsety+movement2,  -self.size+self.offsetz+off),
            (self.size+self.offsetx+movement+widthleft,     self.size+self.offsety+movement2,  self.size+self.offsetz+off),
            (-self.size+self.offsetx+movement+widthright,    self.size+self.offsety+movement2,  self.size+self.offsetz+off),
            (-self.size+self.offsetx+movement+widthright,    self.size+self.offsety+movement2,  -self.size+self.offsetz+off))
        
        return vertices


    def show_cube(self):
        verticles =self.verticlesHause()
        glBegin(GL_QUADS)
        for i, vertex in enumerate(self.surface): 
            wsp = 20/(self.deep)
            colorx = (0, 0, 0.5)
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

    