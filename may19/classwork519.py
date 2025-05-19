# Problem 1: raise number function
def raiseNum(num):
    if(num % 2 == 0):
        print(num ** 3)
    else:
        print(num ** 4)

raiseNum(3)
raiseNum(4)
raiseNum(5)
print()

# Problem 2: string function
def printChars(str):
    # In a 10 character string:
    # -(len(str) - 3) does index -7
    # -(len(str) - 6) does index -4
    print(str[-(len(str) - 3) : -(len(str) - 6)])

printChars("abcdefghij")