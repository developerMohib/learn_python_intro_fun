n = int(input())
given_numbers = list(map(int, input().split()))
sum_of_given = sum(given_numbers)
total_sum = n * (n + 1) // 2
missin_numbers = total_sum - sum_of_given
