#.Write a program to calculate the percentage of student based on marks of any 5 subjects.
sub1 = int(input("enter marks in english : "))
sub2 = int(input("enter marks in hindi : "))
sub3 = int(input("enter marks in maths : "))
sub4 = int(input("enter marks in science : "))
sub5 = int(input("enter marks in computer : "))

total = sub1+sub2+sub3+sub4+sub5
percentage = total/500

print("total marks : ", total)
print("percentage : ", percentage)