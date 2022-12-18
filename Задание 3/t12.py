# title Task
# description N_12
# code
coords = [(-1, 1), (2, -3), (-5, -3), (2, 8), (1, 3)]

ans = sorted([(c[0] ** 2 + c[1] ** 2) ** 0.5 for c in coords if c[0] >= 0 and c[1] >= 0])[-1]
print(ans)