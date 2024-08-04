from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Define vertices and edges of a cube
vertices = [
    [1, 1, 1],
    [-1, 1, 1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, -1],
    [1, -1, -1]
]

edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]

# Rotation angles
angleX, angleY, angleZ = 0, 0, 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -5)

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def display():
    global angleX, angleY, angleZ
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    
    # Apply transformations
    glTranslatef(0.0, 0.0, 0.0)  # Translation
    glRotatef(angleX, 1, 0, 0)  # Rotation around X
    glRotatef(angleY, 0, 1, 0)  # Rotation around Y
    glRotatef(angleZ, 0, 0, 1)  # Rotation around Z
    glScalef(1.0, 1.0, 1.0)     # Scaling
    
    draw_cube()
    glPopMatrix()
    glutSwapBuffers()

def update(value):
    global angleX, angleY, angleZ
    angleX += 1
    angleY += 1
    angleZ += 1
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow("3D Transformations using GLUT")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()


main()
