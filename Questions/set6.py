'''
Q38. Write a program that takes three numbers as input and determines
the largest one using nested if-else statements. Make sure all 3 numbers
entered by user are different.

'''
# I=int(input("Enter I no.: "))
# II=int(input("Enter II no.: "))
# III=int(input("Enter III no.: "))
# if I>II:
#     if I>III:
#         print(f"{I} is larghest")
#     else:
#         print(f"{III} is largest")
# elif II>III:
#     if II>III:
#         print(f"{II} is largest")
# else:
#     print(f"{III} is largest")

'''
Q39. Write a program that checks if a given year is a leap year. Leap years
are divisible by 4, but not by 100 unless they are also divisible by 400.

# '''
# y=int(input("Enter year: "))
# if y%4==0:
#     print(f"{y} is a  leap year")
#     if y%100==0:
#         if y%400==0:
#             print(f"{y} is leap year")
#         else:
#             print(f"{y} is not a leap year")
# else:
#     print(f"{y} is not a leap year")
            
'''
Q40. Create a program that calculates the price of a movie ticket based on
the age of the customer. If the customer is under 12, the ticket costs $5; if
they are between 12 and 65, the ticket costs $10; otherwise, it's $7.

'''
# age=float(input("Enter age: "))
# if age<=65:
#     if age>=12:
#         print(" The ticket costs you $10")
#     else:
#         print("the ticket costs you $5")
# else:
#     print("The ticket costs you $7")

'''
Q41. Write a program that calculates a person's BMI based on their height
(in meters) and weight (in kilograms). Use the following formula: BMI =
weight / (height^2). Then, classify the BMI according to the following
ranges:
QUESTIONS 38 - 41
NESTED IF - ELSE
info@codeanddebug.in Code and Debug codeanddebug.in
Underweight: BMI less than 18.5
Normal weight: BMI 18.5 - 24.9
Overweight: BMI 25 - 29.9
Obesity: BMI 30 or greater
'''

h=float(input("Enter Hieght in meaters: "))
w=float(input("Enter weight in kgs: "))
BMI=w/h**2
if BMI<=24.9:
    if BMI<18.5:
        print("your are underweight.")
    else:
        print("Yor have Normal weight")
else:
    if BMI<29.9:
        print("You are Overweight")
    else:
        print("You fall under Obesity")
