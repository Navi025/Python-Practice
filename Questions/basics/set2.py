# Q4. Write a Python program to add two numbers entered by the user.

#SOL
# num1=int(input("Enter first no.: "))
# num2=int(input("Enter second no.: "))
# Sum=num1+num2
# print(f"Sum of two nos is: {Sum}")

# Q5. Convert a string to an integer and vice versa.

#SOL
# num1=input("Enter first no. : ")
# num2=input("Enter second no.: ")
# concadination=num1+num2 #string
# print(f"Concadination of two nos is: {concadination}") #string
# x=int(num1)
# y=int(num2)
# Sum=x+y
# print(f"The sum of nos is: {Sum} ")

# Q6. Write a Python program to calculate the area of a rectangle using user
# input for length and width.

# l=float(input("Lenght of rectangle = "))
# b=float(input("breadth of rectangle = "))
# a=l*b
# print(f"Area of rectangle = {a}")

# Q7. Write a Python program to calculate the average of three numbers
# entered by the user.

# a=int(input("Enter 1st no.: "))
# b=int(input("Enter 2nd no.: "))
# c=int(input("Enter 3rd no.: "))
# av=(a+b+c)/3
# print(f"The averge = {av}")

# Q8. Convert a float to an integer and vice versa.
# f=884.56
# i=458
# fi=int(f)
# iff=float(i)
# print(f"The int value of {f} is {fi}")
# print(f"the float value of {i} is {iff}")

# Q9. Write a program that converts a temperature in Fahrenheit to Celsius.
# The formula is: Celsius = (Fahrenheit - 32) * 5/9.

# f=float(input("Enter temperature in Fahrenhiet: "))
# C = (f - 32) * 5/9
# print(f"Temperaturein celcius is {C}")

# Q10. Calculate sum of 5 subjects and Find percentage.

# m=int(input("Markks obtained in Maths = "))
# p=int(input("Marks optained in Physics = "))
# c=int(input("Marks optained in Chemistry = "))
# e=int(input("Marks optained in ENglish = "))
# h=int(input("Marks optained in Hindi = "))
# pc=((p+c+m+e+h)/500)*100
# print(f"Total Percentage = {pc}%")

# Q11. Ask number of games played in a tournament. Ask the user number of
# games won and number of games loss. Calculate number of tie and total
# Points. (1 win= 4 points, 1 tie =2 points)

#no of games played
played=int(input("Enter total no of games played: "))
#no of games won
won=int(input("Enter no of games won: "))
#no of game lose
lose=int(input("Entre no of game lose: "))
#no of ties
ties=played-(won+lose)
#total scored points
tsp=(won*4)+(ties*2) 
total=played*4
print(f"Total scored points are {tsp}/{total} with {ties} tie matches")