def drawstring(x, y, z, mystr)
	glRasterPos3f(x,y,z)
	for c in range(len(mystr)):
		glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18,mystr[c])


def frontscreen():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,0,1)
	drawstring(-15,40,0.0,"RNS INSTITUTE OF TECHNOLOGY")
	glColor3f(0.7,0,1)
	drawstring(-30,35,0.0,"DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING")
	glColor3f(1,0.5,0)
	drawstring(-15,30,0.0,"A MINI PROJECT ON ")
	glColor3f(1,0,0)
	drawstring(-25,20,0.0,"PROGRESSION OF TOOTH CARIES")
	glColor3f(1,0.5,0)
	drawstring(-35,0,0.0,"BY:")
	glColor3f(0.5,0,0.5)
	drawstring(-35,-10,0.0,"RADHIKA AGAL (1RN16CS076)")
	drawstring(-35,-12,0.0,"SHWETHA K M (1RN16CS103)")
	strflag=0
	drawstring(-35,-14,0.0,"6th Semester,CSE")
	glColor3f(1,0.5,0)
	drawstring(15,0,0.0,"GUIDE:")
	glColor3f(0.5,0.2,0.2)
	drawstring(15,-10,0.0,"MAMATHA JAJUR")
	strflag=0
	drawstring(15,-14,0.0,"Assistant Professor,CSE")
	glColor3f(1,0.1,1)
	drawstring(-13,-35,0.0,"PRESS ENTER TO START")
	glFlush()
