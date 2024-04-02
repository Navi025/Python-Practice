def tie():
    t=p-(l+w)
    print(f"Total tie matches: {t}")


def Tscore(t):
    ts=w*4+t*2
    print(f"Total score is {ts}")

p=int(input("Enter no of total games played: "))
w=int(input("Enter total no matches won: "))
l=int(input("Enter total no of matches loseL: "))
tie()
Tscore(p-(l+w))