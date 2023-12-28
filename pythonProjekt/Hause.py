from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import Cube
from Roof import Roof
class Hause:
    def __init__(self, cube, roof, door):
        self.cube = cube
        self.roof = roof
        self.door = door

    def move(self, deep):
        self.cube.moveDeep(deep)
        self.roof.moveDeep(deep)
        self.door.moveDeep(deep)

    def showHouse(self):
        self.door.show_cube()
        self.cube.show_cube()
        self.roof.show_triangle()
        
