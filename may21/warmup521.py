# Problem 1: case count thing
def findCaseCount():
    caseCount = 1000000
    i = 0
    while(i < 15):
        caseCount = 1000000 * .54 ** i
        i += 1
        print(caseCount)

findCaseCount()
print()


# Problem 2: max case count based on growth rate
def caseCountWeeks(weeks):
    caseCount = 1000000
    i = 0
    while(i < weeks):
        caseCount = 1000000 * .54 ** i
        i += 1
        print(caseCount)

caseCountWeeks(10)
    