"""
#Count Digits


Brute Force
"""


# x=4596
# Count=len(str(x))
# print(Count)

"""
Better
"""

# def countint(num):
#     c=0
#     n=num
#     while n>0:
#         c+=1
#         n=n//10
#     return (c)

# print(countint(4568))

"""
Optimal
"""

# import math
# def cd(num:int)->int:
#     return math.floor(math.log10(num)+1)
# print(cd(4578))

"""
Recverce a no

Brute Force
"""
# x=4536
# print(int(str(x)[::-1]))

#TC=O(n)
#SC=O(1)

"""
Better
"""

# def reverce(num)->int:
#     result=0
#     n=num
#     while n>0:
#         id=n%10
#         result=(result*10+id)
#         n=n//10
#     return result
# print(reverce(4569))

# TC = O(log10N)
# SC = O(1)

"""
Constrains
-2**31 < x > 2**31-1
"""

def RV(num)->int:
    if num<-2**31 and num>2**31-1:
        return 0
    negative=False
    n=num
    if n<0:
        negative=True
        n=abs(n)
    

    result=0

    while n>0:
        id=n%10
        result=result*10+id
        n=n//10
    if negative==False:
        if result>2**31-1:
            return 0
        return result
    else:
        result=result*-1
        if result<-2**31:
            return 0
        return result

print(RV(-121))
print(RV(1243))  
print(RV(124345698545465465464664745768))    