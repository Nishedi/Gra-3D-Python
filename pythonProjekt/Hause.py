from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import Cube
from Roof import Roof
class Hause:
    def __init__(self, cube, roof):
        self.cube = cube
        self.roof = roof

    def move(self, deep):
        self.cube.moveDeep(deep)
        self.roof.moveDeep(deep)

    def showHouse(self):
        self.cube.show_cube()
        self.roof.show_triangle()
