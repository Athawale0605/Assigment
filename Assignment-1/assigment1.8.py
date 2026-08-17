#.write a program to covert days into years, weeks and days.

#.Input total number of days 
days = int(input("Enter number of days:"))

#.Calculate years, weeks, and remaining days
years = days // 365 
remaining_days = days % 365 
weeks = remaining_days // 7
days_left = remaining_days % 7

#Display the result 
print("years =", years)
print("weeks =", weeks)
print("days =", days_left)
 