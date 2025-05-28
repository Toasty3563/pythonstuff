# Precondition: arr is a 5x5 2D array
def appendAndAddElements(arr):
    total = 0
    results = []
    for row in range(len(arr)):
        if(row == 0):
            results.append(arr[row][0])
            results.append(arr[row][2])
        elif(row == 1):
            results.append(arr[row][0])
            results.append(arr[row][3])
        elif(row == 2):
            results.append(arr[row][0])
            results.append(arr[row][2])
            results.append(arr[row][3])
            results.append(arr[row][4])
        elif(row == 3):
            results.append(arr[row][2])
        elif(row == 4):
            results.append(arr[row][1])
            results.append(arr[row][4])
    
    for i in results:
        total += i
    return total

arr = [ [0, 10, 7, 5, 3],
        [2, 50, 40, 2, 1], 
        [6, 4, 15, 10, 8],
        [30, 41, 47, 51, 60],
        [1, 2, 3, 4, 5] ]
print(appendAndAddElements(arr))