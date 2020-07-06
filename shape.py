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

'''

def rect(b, h):
	'''
	FUNCTION 	rect
		@args: b, h -> Int or float
		@returns: Int or float
	'''
	return b * h

def circle(r, Pi = 3.142):
	'''
	FUNCTION 	circle
		@args: r, Pi-> Int or float
		@returns: Int or float
	'''
	return Pi * (r**2)

def square(s):
	'''
	FUNCTION 	square
		@args: s -> Int or float
		@returns: Int or float
	'''
	return s ** 2

def trapezoid(a, b, h):
	'''
	FUNCTION 	trapezoid
		@args: a,b, h -> Int or float
		@returns: Int or float
	'''
	return ((a + b)* h) / 2

def ellipse(a, b, Pi = 3.142):
	'''
	FUNCTION 	ellipse
		@args: a,b, Pi -> Int or float
		@returns: Int or float
	'''
	return Pi * a * b

def triangle(b,h):
	'''
	FUNCTION 	triangle
		@args: b, h -> Int or float
		@returns: Int or float
	'''
	return 0.5 * b * h

def parallelogram(b,h):
	'''
	FUNCTION 	parallelogram
		@args: b, h -> Int or float
		@returns: Int or float
	'''
	return 0.5 * b * h	
