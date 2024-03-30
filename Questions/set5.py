# Q27. Write a program to check if the number is ODD, EVEN or Equal to Zero.
# n=int(input("Enter a whole no:  "))
# if n==0:
#     print(f"The number is Zero")
# elif n%2==0:
#     print(f"{n} in even")
# else:
#     print(f"{n} is odd")

# Q28. Write a program to check if number is divisible by 2 and 3 but not 8.

# n=int(input("Enter a number: "))
# if n%2==0 and n%3==0 and n%8!=0:
#     print("This no is divisible by 2 and 3 but nit by 8")
# else:
#     print("This number is not the requied number.")

'''
Q29. Write a program to print the last digit of a number. (NOT A IF ELSE
QUESTION)
'''
# n=int(input("Enter a number: "))
# a=n%10
# print(f"The last digit of {n} is {a}")

'''
 Q30. Write a program to check if the last digit of a number is divisible by 5
or not.
'''
# n=int(input("Enter a number: "))
# a=n%10
# if a%5==0:
#     print(f"The last digit of {n} in divisible by 5")
# else:
#     print(f"The last digit of {n} is not divisible by 5")

'''
Q31. Write a program to calculate bill. Ask the final amount from the user.
You have to give discount and print the final bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the final amount to be paid
'''
# a=float(input("Enter Total amount: "))
# if a>50000:
#     d=0.3*a
#     fa=a-d
# elif a>40000 and a<49999:
#     d=0.25*a
#     fa=a-d
# elif a>30000 and a<39999:
#     d=0.2*a
#     fa=a-d
# elif a>10000 and a<29999:
#     d=0.1*a
#     fa=a-d
# elif a>1 and a<9999:
#     d=0.0
#     fa=a
# else:
#     d=0.0
#     fa=0.0
#     print("You have entered incorrect amount")

# print(f"You Got dicount of Rs {d:.2f}\nTotal payable amount = Rs {fa:.2f}")

# Q32. Ask 4 numbers from user. Make sure all the numbers entered by user
# are different. Print which number is the smallest.

# d=int(input("Enter I no.: "))
# a=int(input("Enter II no.: "))
# b=int(input("Enter III no.: "))
# c=int(input("Enter IV no.: "))
# if a<b and a<c and a<d:
#     print(f"{a} is smallest")
# elif b<a and b<c and b<d:
#     print(f"{b} is smallest")
# elif c<a and c<b and c<d:
#     print(f"{c} is smallest")
# else:
#     print(f"{d} is smallest") 

'''
Print “Fizz” if the number is divisible by 3.
Print “Buzz” if the number is divisible by 5.
Print “FizzBuzz” if the number is divisible by 3 and 5.
Print the number itself if none of the conditions are true.

'''
# n=int(input("Enter a number: "))
# if n%3 and n%5:
#     print("FizzBuzz")
# elif n%3:
#     print("Fizz")
# elif n%5:
#     print("Buzz")
# else:
#     print(f"{n}")

'''
Q37. An extra day is added to the calendar almost every four years as
February 29, and the day is called a leap day. A leap year contains a leap
day.
These are the conditions used to identify leap years:
This means the years 2000 and 2400 are leap years, while 1800, 1900,
2100, 2200, 2300 and 2500 are NOT leap years.
Ask a year input from user. And tell if the year entered by user is leap or
not.
if the year can be evenly divided by 4, it is then a leap year
but if the year is evenly divided by 4 and also by 100, then it is NOT a
leap year
but if the year is evenly divided by 4 and also by 400, then it is a leap
year
'''

y=int(input("Enter a year: "))
if y%4==0 and y%100==0:
    print(f"{y} is not a leap year.")
elif y%4==0:
    print(f"{y} is leap year")
elif y%4==0 and y%400==0:
    print(f"{y} is a leap year")
else:
    print(f"{y} in not a leap .")