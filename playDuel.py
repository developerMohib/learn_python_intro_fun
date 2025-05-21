t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    liar_found = False

    for i in range(n - 1):
        if a[i] == 0 and a[i + 1] == 0:
            liar_found = True
            break

    if liar_found:
        print("YES")
    else:
        print("NO")
