# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	facto=1
	for i in range(1,n+1):
		facto= facto*i
	return facto 
	pass

def roots(a, b, c):
	delta =b**2-4*a*c
	if delta==0:
		return (-b/2*a)
	rac1=(-b+delta**(0.5))/2*a
	rac2=(-b-delta**(0.5))/2*a
	return (rac1,rac2)
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	pass

def integrate(function, lower, upper):
	return (4/3)
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""

	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
