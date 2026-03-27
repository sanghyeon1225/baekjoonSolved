n = int(input())

data = [input() for _ in range(n)]

kbs1_index = data.index("KBS1")
kbs2_index = data.index("KBS2")

answer = ''
if (kbs1_index < kbs2_index):
    answer += '1' * kbs1_index

    answer += '4' * kbs1_index

    answer += '1' * kbs2_index

    answer += '4' * (kbs2_index - 1)
else:
    answer += '1' * kbs1_index

    answer += '4' * kbs1_index

    answer += '1' * (kbs2_index + 1)

    answer += '4' * kbs2_index

print(int(answer))