# title Task
# description N_5
# code
# {a, e, i, o, u, y}
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed " \
         "thought "

ans = ''.join([x for x in string[:] if x not in {'a', 'e', 'i', 'o', 'u', 'y'}])
print(ans)
