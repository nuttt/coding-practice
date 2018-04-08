t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    a_even = sorted(a[0::2])
    a_odd = sorted(a[1::2])
    b = []
    for i in range(0, len(a_even)):
        b.append(a_even[i])
        if i < len(a_odd):
            b.append(a_odd[i])
    idx = None
    for i in range(0, len(b) - 1):
        if b[i] > b[i+1]:
            idx = i
            break

    if idx is None:
        print("Case #{}: {}".format(ti, "OK"))
    else:
        print("Case #{}: {}".format(ti, idx))
