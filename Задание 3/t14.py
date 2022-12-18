# title Task
# description N_14
# code
nums = ['43141', '32441', '431', '4154', '43121']

ans = list(filter(lambda x: True if x ** 2 % 2 == 0 else False, map(int, nums)))
print(ans)