# title Task
# description N_10
# code
coords = [(1, 1), (2, 3), (5, 3), (2, 8), (1, 3)]

ans = {c: (c[0] ** 2 + c[1] ** 2) ** 0.5 for c in [c for c in coords if (c[0] * 5 - 2) == c[1]]}
print(ans)
