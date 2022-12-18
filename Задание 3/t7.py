# title Task
# description N_7
# code
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed " \
         "thought "

ans = {k: len(k) for k in string.split(' ')}
print(ans)
