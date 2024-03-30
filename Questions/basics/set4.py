# Q23. Write a Python program that takes an integer input and prints
# whether it's positive, negative. (Consider 0 as positive)

# x=int(input("Enter an integer: "))
# if x>=0:
#     print("It is a positive integer")
# else:
#     print("It is a negetive integer")



#Q24. Write a program that takes a character as input and prints whether
# it's a vowel or a consonant. (Multiple OR will be used)

# l=input("Enter a character: ")
# if l=="a" or l=="e" or l=="i" or l=="o" or l=="u":
#     print("It is a vowel")
# else:
#     print("it is a conconent.")



# Q25. Write a program that takes two numbers as input and checks if the
# first number is divisible by the second.

# num1=int(input("Enter I no: "))
# num2=int(input("Enter II no: "))
# if num1%num2==0:
#     print(f"{num1} in completely divisible by {num2}")
# else:
#     print(f"{num1} is completely not divisle by {num2}")



# Q26. A student will not be allowed to sit in exam if his/her attendance is
# less than 75%
# Take following input from user
# QUESTIONS 23-26
# IF - ELSE
# info@codeanddebug.in Code and Debug codeanddebug.in
# Number of classes held
# Number of classes attended.
# 1. Print percentage of class attended
# 2. Print Is student is allowed to sit in exam or not.

ch=int(input("Enter the no of classes held = "))
ca=int(input("Enter the no of classes attended = "))
at=(ca/ch)*100.0
print(f"Attendence = {at:.2f}%")
if at>=75:
    print("Student is elegible for exam.")
else:
    print("Student is \"NOT\" elegible for exams.")