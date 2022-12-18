# title Task
# description N_13
# code
nums_first, nums_second = [1, 2, 3, 5, 8], [2, 4, 8, 16, 32]

ans = list(map(lambda x: (x[0] + x[1], x[0] - x[1]), zip(nums_first, nums_second)))
print(ans)