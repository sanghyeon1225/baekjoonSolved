def solution(numbers):
    numbers = sorted(numbers)
    first = numbers[0] * numbers[1]
    last = numbers[-1] * numbers[-2]
    return(max(first,last))