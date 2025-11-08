import itertools

n = int(input())

s = ''


for i in range(n):
    s += str(i+1)

test = list(itertools.permutations(list(s), n))

for i in range(len(test)):
    print(' '.join(test[i]))
    