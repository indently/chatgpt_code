from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Define the vertices of the cube
vertices = ((-1, -1, -1), (-1, 1, -1), (1, 1, -1), (1, -1, -1), (-1, -1, 1), (-1, 1, 1), (1, 1, 1), (1, -1, 1))

# Define the edges of the cube
edges = ((0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 3), (2, 6), (3, 7), (4, 5), (4, 7), (5, 6), (6, 7))

# Define the initial rotation angle
angle = 0


def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 50)
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
    glRotatef(angle, 2, 1, 1)  # Rotate the cube around the x, y, and z axes
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    glutSwapBuffers()
    angle += 0.5  # Increment the rotation angle


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow("3D Cube")
glutDisplayFunc(display)
glEnable(GL_DEPTH_TEST)
glClearColor(0, 0, 0, 1)
glutIdleFunc(glutPostRedisplay)  # Redraw the display continuously
glutMainLoop()
