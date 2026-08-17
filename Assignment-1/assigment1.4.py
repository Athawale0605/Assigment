#write a program  to enter P,T,R and calculate simple interest.

p = float(input("enter principal (p): "))
t = float(input("enter time (t) in years: "))
r = float(input("enter rate (r): "))

si = (p*t*r) / 100
print("Simple Interest = ", si)