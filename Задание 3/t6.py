# title Task
# description N_6
# code
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed " \
         "thought "

ans = [x for x in string.split(' ') if len(x) <= 5]
print(ans)