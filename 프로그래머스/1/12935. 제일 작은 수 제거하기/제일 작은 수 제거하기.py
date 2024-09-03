def solution(arr):
    index = 0
    min = arr[0]
    if(len(arr) == 1):
        return [-1]
    for i in range(len(arr)):
        if (arr[i] < min):
            index = i
            min = arr[i]
            
    arr.remove(arr[index])
    return arr