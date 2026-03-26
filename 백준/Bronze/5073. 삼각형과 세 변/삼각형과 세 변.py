while(1):
    a, b, c = map(int, input().split())
    if (a == 0 and b == 0 and c == 0):
        exit()
    
    if (a == b == c):
        print("Equilateral")
    elif (((a + b + c) - (2 * max(a, b, c))) > 0):
        if (a == b or b == c or a == c):
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")

        