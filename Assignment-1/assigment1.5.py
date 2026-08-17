#write a program to enter P, T, R and calculate compound interest.

P = float(input("Enter principal (P): "))
T = float(input("Enter time (T) in years: "))
R = float(input("Enter rate (R): "))

A = P * (1 + R / 100)**T
CI = A - P 
print("Compound Interest = ", CI)
print("Amount =", A)