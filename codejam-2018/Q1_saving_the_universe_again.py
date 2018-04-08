t = int(input())
for ti in range(1, t + 1):
    d, command = input().split(" ")
    d = int(d)

    # get total damage first
    charge = 0
    shoot = 0
    damage = 0
    for c in command:
        if c == "C":
            charge += 1
        else:
            shoot += 1
            damage += 2 ** charge

    if shoot > d:
        print("Case #{}: {}".format(ti, "IMPOSSIBLE"))
        continue
    if damage <= d:
        print("Case #{}: {}".format(ti, 0))
        continue

    s_count = 0
    swap_count = 0
    min_swap = None
    for c in command[::-1]:
        if c == "S":
            s_count += 1
        else:
            for i in range(0, s_count):
                damage -= 2 ** (charge - 1)
                swap_count += 1
                if damage <= d and min_swap is None:
                    min_swap = swap_count
            charge -= 1

    print("Case #{}: {}".format(ti, min_swap))



