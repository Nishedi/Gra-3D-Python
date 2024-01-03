from math import cos, sin, radians
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Tree:
    def __init__(self, trunk_height, trunk_radius, branch_length, branch_radius):
        self.trunk_height = trunk_height
        self.trunk_radius = trunk_radius
        self.branch_length = branch_length
        self.branch_radius = branch_radius

    def draw_tree(self, x, y, z):
        # Draw trunk
        glColor3fv((0.5, 0.35, 0.05))
        gluCylinder(gluNewQuadric(), self.trunk_radius, self.trunk_radius, self.trunk_height, 16, 16)

        # Draw branches
        for i in range(6):
            angle = i * (360 / 6)  # Angle between each branch
            x_offset = self.branch_length * cos(radians(angle))
            y_offset = self.branch_length * sin(radians(angle))

            glBegin(GL_QUADS)
            glColor3fv((0, 1, 0))  # Green color for branches
            glVertex3f(x + x_offset - self.branch_radius, y + y_offset, z)
            glVertex3f(x + x_offset + self.branch_radius, y + y_offset, z)
            glVertex3f(x + x_offset + self.branch_radius, y + y_offset, z + self.branch_length)
            glVertex3f(x + x_offset - self.branch_radius, y + y_offset, z + self.branch_length)
            glEnd()
