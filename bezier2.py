from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pow

class Point:

  def __init__(self, id, x, y, z):
  	self.x = x
  	self.y = y
  	self.z = z
  	self.id = id

  def PrintPoint(self):
    print("Point %d = <%f, %f, %f>\n" %(self.id, self.x, self.y, self.z))
    

def drawCurve():
  glClearColor(0.0, 0.0, 0.0, 0.0)
  glShadeModel(GL_FLAT)


def bezierCurve(t, P0,P1, P2, P3, P4) :
    #point = (pow((1-t), 3.0) * P0) +(3 * pow((1-t),2) * t * P1) +    (3 * (1-t) * t * t * P2) + (pow(t, 3) * P3)
    point = (pow((1-t), 4.0) * P0) +(4 * pow((1-t),3) * t * P1) +    (4 * pow((1-t),2) * t * t * P2) + (4 * (1-t) * t**3 * P3)+(pow(t, 4) * P4)
    
    #point = ((pow((1-t),7.0) * P0) + (7 * pow((1-t), 6.0) * P1 * t) + (7 * pow((1-t), 5.0) * P2 * t**2) + (7 * pow( (1-t), 4.0) * P3 * t**3)+ (7 * pow( (1-t), 3.0) * P4 * t**4) + (7 * pow( (1-t), 2.0) * P5 * t**5) + (7 * pow( (1-t), 1.0) * P6 * t**6) + (7 * pow( (1-t), 0.0) * P7 * t**7))
    
    return point


def plotcurve():
  start=Point(0, -5, 0, 0)
  tan1=Point(1, -7, 3, 0)
  tan2=Point(2, -4, 6, 0)
  tan3=Point(3,-1,1,0)
  end=Point(4, 0, 2, 0)
  #tan4=Point(4, 1, 1, 0)
  #tan5=Point(5, 4, 6, 0)
  #tan6=Point(6, 7, 3, 0)
  #end=Point(7, 5, 2, 0)

  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1.0, 1.0, 1.0)
  glPointSize(5.0)
  glColor3f(1.0, 1.0, 1.0)
  t = 30
  glBegin(GL_POINTS)
  for i in range (31):
    pos = i/t
    x = bezierCurve(pos, start.x, tan1.x, tan2.x, tan3.x, end.x)
    #x = bezierCurve(pos, start.x, tan1.x, tan2.x, tan3.x, tan4.x, tan5.x, tan6.x,end.x)
    y = bezierCurve(pos, start.y, tan1.y, tan2.y, tan3.y, end.y)
    #y = bezierCurve(pos, start.y, tan1.y, tan2.y, tan3.y, tan4.y, tan5.y, tan6.y, end.y)
    #In our case, the z should always be empty
    z = bezierCurve(pos, start.z, tan1.z, tan2.z, tan3.z, end.z)
    #z = bezierCurve(pos, start.z, tan1.z, tan2.z, tan3.z, tan4.z, tan5.z, tan6.z,end.z)
    result=Point(4, x, y, z)
    result.PrintPoint()
    glVertex3f(x, y, z)
  
  glEnd()
  
  glFlush()
  
  
  
'''def display():
	start=Point(0, -5, 0, 0)
	tan1=Point(1, -7, 3, 0)
	tan2=Point(2, -4, 6, 0)
	tan3=Point(3, -1, 1, 0)
	end=Point(4, 0, 2, 0)
	plotcurve(start,tan1,tan2,tan3,end)
	start=Point(0, 5, 0, 0)
	tan1=Point(1, 7, 3, 0)
	tan2=Point(2, 4, 6, 0)
	tan3=Point(3, 1, 1, 0)
	end=Point(4, 0, 2, 0)
	plotcurve(start,tan1,tan2,tan3,end)'''
  

'''def display2():
  start=Point(0, 5, 0, 0)
  tan1=Point(1, 7, 3, 0)
  tan2=Point(2, 4, 6, 0)
  tan3=Point(3, 1, 1, 0)
  end=Point(4, 0, 2, 0)

  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(1.0, 1.0, 1.0)
  glPointSize(5.0)
  glColor3f(1.0, 1.0, 0.0)
  t = 30
  glBegin(GL_POINTS)
  for i in range (31):
    pos = i/t
    x = bezierCurve(pos, start.x, tan1.x, tan2.x, tan3.x, end.x)
    y = bezierCurve(pos, start.y, tan1.y, tan2.y, tan3.y, end.y)
    #In our case, the z should always be empty
    z = bezierCurve(pos, start.z, tan1.z, tan2.z, tan3.z, end.z)
    result=Point(4, x, y, z)
    result.PrintPoint()
    glVertex3f(x, y, z)
  
  glEnd()

  
  glFlush()'''



def reshape(w,h):
  glViewport(0, 0, w, h)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  #glOrtho scales the matrix by multiplying the matrix
  if (w <= h):
  	glOrtho(-5.0, 5.0, -5.0*h/w, 5.0*h/w, -5.0, 5.0);
  
  else :
  	glOrtho(-5.0*w/h,5.0*w/h, -5.0, 5.0, -5.0, 5.0);
  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()


def main():
  glutInit()
  glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize (640, 480)
  glutInitWindowPosition (100, 100)
  glutCreateWindow ('b')

  drawCurve()

  glutDisplayFunc(plotcurve)
  
  
  glutReshapeFunc(reshape)
  glutMainLoop()
  
main()

