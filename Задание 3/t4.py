# title Task
# description N_4
# code
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
ans = len([x for x in filter(lambda x: True if x == ' ' else False, string[:])])
print(ans)