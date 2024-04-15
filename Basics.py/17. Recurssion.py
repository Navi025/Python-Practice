#print 1-n
def func(i, n):
    if i > n:
        return
    print(i)
    func(i + 1, n)

func(1, 10)

# Print 1-n iwthout usinf i+1
def func(i, n):
    if i < 1:       #using backtracking
        return
    func(i - 1, n)
    print(i)

func(4, 4)

# Print sum of 1 - N using recurssion -- Parameterised Way
def func(i, sum):
    if i < 1:
        print(sum)
        return
    func(i - 1, sum + i)

func(10, 0)


# Print sum of 1 - N using recurssion -- Functionalw Way
def func(num):
    if num < 0:
        raise Exception("Invalid Value")
    if num == 0:
        return 0
    return num + func(num - 1)

x = func(1.5)
print(x)