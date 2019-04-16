from math import pow

class Point:

  def __init__(self, id, x, y, z):
  	self.x = x
  	self.y = y
  	self.z = z
  	self.id = id

  def PrintPoint(self):
    print("Point %d = <%f, %f, %f>\n" %(self.id, self.x, self.y, self.z))


def beziercurve(t, points):
	l = len(points)
	t_1 = 1 - t
	s = pow(t_1, l-1) * points[0]
	for i in range(l):
		s += (l-1) * pow(t_1, 


def main():
	points = []

	n = int(input("enter no of points"))
	for i in range(n):
		point = input().split()
		points.append(Point(point[0], point[1], point[2], point[3]))
		
	t = int(input("Enter t"))
	print(points)
	#for i in range(len(points)):
		#beziercurve(t, i.x, i.
			
main()
