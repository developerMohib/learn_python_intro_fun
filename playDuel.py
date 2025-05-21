p = int(input())  # test or count play with others
for _ in range(p):
    n = int(input())  # number of player
    a = list(map(int, input().split()))  # win list or lose list of player
    total_wins = sum(a)
    if total_wins > n - 1 or total_wins == 0:
        print("YES")
    else:
        print("NO")
