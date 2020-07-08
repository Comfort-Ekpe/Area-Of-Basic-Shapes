'''
Helps on shape module
NAME:
	shape.py
DESCRIPTION:
	This module helps to find the Area of several shapes. It is used on basic shapes.
	Shapes such as:
	-> Rectangle
	-> Circle
	-> Square
	-> Trapezoid
	-> Ellipse
	-> Triangle
	-> Parallelogram
FUNCTIONS:
	-> Area Of Rectangle
		This finds the area of a rectangle using the formula A = bh
	-> Area Of Circle
		This finds the area of a Circle using the formula A = Pir.sqr
	-> Area Of Square
		This finds the area of a Square using the formula A = s.sqr
	-> Area Of Trapezoid
		This finds the area of a Trapezoid using the formula A = a + b/2 * h
	-> Area Of Ellipse
		This finds the area of a Ellipse using the formula A = Pi a * b
	-> Area Of Triangle
		This finds the area of a Triangle using the formula A = 1/2b*h
	-> Area Of Parallelogram
		This finds the area of a Parallelogram using the formula A = bh
	-> Area of Sector
		This finds the area of a sector using the formula 1/2 r**2 * angle

'''

def findAreaOfRectangle(b, h):
	'''
	FUNCTION NAME:	rect
		This function computes the area of a rectangle which is the base times the  height
		b = distance along the base of the rectangle
		h = vertical height of the rectangle
			@args: b, h -> Int or float
			@returns: Int or float
	'''
	return b * h

def findAreaOfCircle(r, Pi = 3.142):
	'''
	FUNCTION NAME:	circle
		This function computes the area of a circel which is Pi times the radius of the circle
		r = radius of the circle measured in meters or centimeters
		Pi = a constant which has the value f 22/7 or 3.142
			@args: r, Pi-> Int or float
			@returns: Int or float
			'''
	return Pi * (r**2)

def findAreaOfSquare(s):
	'''
	FUNCTION NAME:	square
		This function computes the area of a square which is the square of the sides since all sides are equal
		s = sides of the square
		@args: s -> Int or float
		@returns: Int or float
	'''
	return s ** 2

def findAreaOfTrapezoid(a, b, h):
	'''
	FUNCTION NAME: 	trapezoid
h	This function computes the area of a trapezoid which is the average of the two base lenght times the altitude
	a = upper base
	b = lower base
	h = height of the trapezoid
		@args: a,b, h -> Int or float
		@returns: Int or float
	'''
	return ((a + b)* h) / 2

def findAreaOfEllipse(a, b, Pi = 3.142):
	'''
	FUNCTION NAME: 	ellipse
	This function computes the area of an ellipse which is the bases times Pi
	a = first base
	b = second base
	Pi = constant value 
		@args: a,b, Pi -> Int or float
		@returns: Int or float
	'''
	return Pi * a * b

def findAreaOfTriangle(b,h):
	'''
	FUNCTION NAME: 	triangle
	This function computes the area of a triangle which is half of the base times the  height
		b = distance along the base of the triangle
		h = vertical height of the triangle measured at right angles to the base
			@args: b, h -> Int or float
			@returns: Int or float
	'''
	return 0.5 * b * h

def findAreaOfParallelogram(b,h):
	'''
	FUNCTION NAME: 	parallelogram
	This function computes the area of a parallelogram which is the base times the  height
		b = distance along the base of the parallelogram
		h = vertical height of the parallelogram 
			@args: b, h -> Int or float
			@returns: Int or float
	'''
	return 0.5 * b * h	


def findsectorOfACircle(v, r):
	'''
	FUNCTION NAME:	sector
	This function computes the area of a sector which is the average of the angle in radian times the radius
		@args: b, h -> Int or float
		@returns: Int or float
	'''
	v = int(input("Enter the angle in radians of the sector: "))
	return 0.5 * (r ** 2) * v

