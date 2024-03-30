# age=float(input("Enter age = "))
# if age>=18:
#     print("You can vote")
# else:
#     print("You cannot vote")


# a=int(input("Enter first no = "))
# b= int(input("Enter 2nd no = "))
# if a>b:
#     print(f"{a} is greater")
# else:
#     print(f"{b} is greater")

# a=int(input("Enter teh number = "))
# if a%2 is 0:
#     print(f"{a} is even")
# else: 
#     print(f"{a} is odd")

# p=int(input("Enter marks optained in Physics = "))
# c=int(input("Enter marks optaind in Chemistry = "))
# if p>=33 and c>=33:
#     print("Student is pass")
# else:
#     print("yudent is fail")

'''
Ask 5 subtect's marks 
calculate percentage
91-100 A grade
81-90 B Grade
71-80 C Grade
61-70 D grade
1-60 Fali
INVALSID
'''
# Hindi=int(input("Enter marks optained in Hindi = "))
# English=int(input("Enter marks optained in English = "))
# maths=int(input("Enter marks optained in maths = "))
# Physics=int(input("Enter marks optained in Physics = "))
# Chemistry=int(input("Enter marks optained in Chemistry = "))
# p=((Hindi+English+maths+Physics+Chemistry)/500)*100
# print(f"Percentage = {p:.2f}%")
# if p>=91 and p<=100:
#     print("Grade = A")
# elif p>=81 and p<=91:
#     print("Grade = B")
# elif p>=71 and p<=80:
#     print("Grade = C")
# elif p>=61 and p<=70:
#     print("Grade = D")
# elif p>=1 and p<=60:
#     print("Fail")
# else: 
#     print("INVALID Marks Entered")

'''
NESTED IF ELSE

'''
n=int(input("ENter a number"))
if n>=0:
    if n>0:
        print("no is positive")
    else:
        print("no is equal to zero.")
else:
    print("number is negetive")
