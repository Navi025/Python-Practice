"""
Q1. Write a program that takes two numbers as input and checks if the first
num`1   qaber is divisible by the second.
"""
def div(n1,n2):
    if n1%n2==0:
        print(f"{n1} is divisible by {n2}.")
    else:
        print(f"{n1} is not divisible by {n2}.")

n1=int(input("Enter I no.: "))
n2=int(input("Enter II no.: "))
div(n1,n2)
"""
Q2. A student will not be allowed to sit in exam if his/her attendance is less
than 75%.
Take following input from user
 - Number of classes held
 - Number of classes attended
1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not.
"""
# def permission(at):
#     if at>=75:
#         print("The student i sallowed to sit into the exam.")
#     else:
#         print("The student is not allowed to sit into the exam.")
# def attendence(h,a):
#     at=(a/h)*100
#     print(f"The attendence is: {at:.2f}%")
   

# h=int(input("Total no of classes held: "))
# a=int(input("No of classes attended: "))
# at=attendence(h,a)
# permission(at)
"""
"""