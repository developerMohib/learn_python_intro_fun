p  = int(input())  # p for player 
for _ in range(p)
n = int(input())  # player count
a = list(map(int, input().split()))
total_wins = sum(a)
if total_wins > n-1 or total_wins == 0 :
print('YES')
else:
print('NO')
