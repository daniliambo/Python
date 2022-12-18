# title Task
# description N_16
# code
a = [[11.9, 12.2, 12.9],
     [15.3, 15.1, 15.1],
     [16.3, 16.5, 16.5],
     [17.7, 17.5, 18.1]]

a_sum = list(map(sum, [[x[i] for x in a] for i in range(len(a[0]))]))
print(a_sum)