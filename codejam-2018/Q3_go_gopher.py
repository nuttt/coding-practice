import sys

t = int(input())
for ti in range(1, t + 1):
    A = int(input())
    I = None
    J = None
    if A == 20:
        I, J = 5, 4
    else:
        I, J = 15, 14

    digged = [[False for _ in range(J)] for _ in range(I)]

    while True:
        # get most undigged area
        dig_i, dig_j = 1, 1
        max_undig = 0
        for i in range(1, I - 1):
            for j in range(1, J - 1):
                count = 0
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        if not digged[ii][jj]:
                            count += 1
                if count > max_undig:
                    max_undig = count
                    dig_i, dig_j = i, j
        print(dig_i + 1, dig_j + 1)
        sys.stdout.flush()
        i, j = [int(x) for x in input().split(" ")]
        if i == 0 and j == 0:
            break
        elif i == -1 and j == -1:
            break
        digged[i-1][j-1] = True



