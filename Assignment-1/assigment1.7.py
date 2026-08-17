# Program to find the root of a Quadratic Equation.
import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / 2*a 
    root2 = (-b - math.sqrt(d))/ 2*a
    print("the roots are real and different.")
    print("root1 =", root1)
    print("root2 =", root2)

elif d == 0:
    root = -b / 2*a
    print("roots are real and equal.")
    print("root =", root)

else:
    real = -b / 2*a
    imaginary = math.sqrt(-d)/ 2*a
    print("Roots are complex. ")
    print("Root 1 =", real, "+", imaginary, "i")
    print("Root 2 =", real, "-", imaginary, "i")

  
