str1 = " " + input()
str2 = " " + input()

LCS = [[0] * len(str2) for _ in range(len(str1))]

for i in range(len(str1)):
    for j in range(len(str2)):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif str1[i] == str2[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[len(str1)-1][len(str2)-1])
