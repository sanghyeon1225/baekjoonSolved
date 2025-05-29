text = input()
explode = input()

stack = []

for i in text:
    stack.append(i)
    
    if((stack[-1] == explode[-1]) and ''.join(stack[-len(explode):]) == explode):
        del stack[-len(explode):]

if (stack):
    print(''.join(stack))
else:
    print("FRULA")
    