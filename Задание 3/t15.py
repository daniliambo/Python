# title Task
# description N_15
# code
import json

input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""

d = {x.split(",")[0]: x.split(",")[1:] for x in input_str.split()}
print(json.dumps([{j: d[j][k] for j in d.keys()} for k in range(len(d.keys()))], indent=2))
