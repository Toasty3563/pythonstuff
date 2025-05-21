# Problem 1: case count thing
def findCaseCount():
    caseCount = 1000000
    i = 0
    while(i < 15):
        caseCount = 1000000 * .54 ** i
        i += 1
    return caseCount

print(findCaseCount() + "\n")

# Problem 2: max case count based on growth rate
def caseCountWeeks(weeks):
    caseCount = 1000000
    i = 0
    while(i < weeks):
        caseCount = 1000000 * .54 ** i
        i += 1
    return caseCount

print(caseCountWeeks(10))

# Problem 3: 2d int array
def sumArray(arr):
    min = float('inf')
    minRow = []
    for row in arr:
        rowSum = sum(row)
        if(rowSum < min):
            min = rowSum
            minRow = row
    print("Row with smallest sum: ", minRow)
    print("Smallest sum: ", min)

arr = [[3, 1, 4, 1, 5],
       [9, 2, 6, 5, 3],
       [5, 8, 9, 7, 9],
       [1, 1, 1, 1, 1]]
sumArray(arr)