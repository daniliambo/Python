# Задание 3

+ [Task](#Task)
+ [Task](#Task)
+ [Task](#Task)
+ [Task](#Task)
+ [Task](#Task)
+ [Task](#Task)
+ [Task](#Task)
+ [Task](#Task)
+ [Task](#Task)
+ [Task](#Task)
+ [Task](#Task)
+ [Task](#Task)
+ [Task](#Task)
+ [Task](#Task)
+ [Task](#Task)
+ [Task](#Task)

## Task

 N_4

```python
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
ans = len([x for x in filter(lambda x: True if x == ' ' else False, string[:])])
print(ans)
```

## Task

 N_12

```python
coords = [(-1, 1), (2, -3), (-5, -3), (2, 8), (1, 3)]

ans = sorted([(c[0] ** 2 + c[1] ** 2) ** 0.5 for c in coords if c[0] >= 0 and c[1] >= 0])[-1]
print(ans)
```

## Task

 N_16

```python
a = [[11.9, 12.2, 12.9],
     [15.3, 15.1, 15.1],
     [16.3, 16.5, 16.5],
     [17.7, 17.5, 18.1]]

a_sum = list(map(sum, [[x[i] for x in a] for i in range(len(a[0]))]))
print(a_sum)
```

## Task

 N_1

```python
ans = [i for i in range(1, 1000) if i % 17 == 0]
print(ans)
```

## Task

 N_5

```python
# {a, e, i, o, u, y}
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed " \
         "thought "

ans = ''.join([x for x in string[:] if x not in {'a', 'e', 'i', 'o', 'u', 'y'}])
print(ans)

```

## Task

 N_13

```python
nums_first, nums_second = [1, 2, 3, 5, 8], [2, 4, 8, 16, 32]

ans = list(map(lambda x: (x[0] + x[1], x[0] - x[1]), zip(nums_first, nums_second)))
print(ans)
```

## Task

 N_8

```python
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed " \
         "thought "

ans = {x for x in string[:]}
print(ans)
```

## Task

 N_9

```python
l = [1, 2, 3, 4]

ans = [x ** 2 for x in l]
print(ans)
```

## Task

 N_2

```python
ans = [i for i in range(1, 1000) if str(i).find('2') != -1]
print(ans)

```

## Task

 N_14

```python
nums = ['43141', '32441', '431', '4154', '43121']

ans = list(filter(lambda x: True if x ** 2 % 2 == 0 else False, map(int, nums)))
print(ans)
```

## Task

 N_6

```python
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed " \
         "thought "

ans = [x for x in string.split(' ') if len(x) <= 5]
print(ans)
```

## Task

 N_10

```python
coords = [(1, 1), (2, 3), (5, 3), (2, 8), (1, 3)]

ans = {c: (c[0] ** 2 + c[1] ** 2) ** 0.5 for c in [c for c in coords if (c[0] * 5 - 2) == c[1]]}
print(ans)

```

## Task

 N_7

```python
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed " \
         "thought "

ans = {k: len(k) for k in string.split(' ')}
print(ans)

```

## Task

 N_11

```python
ans = [x ** 2 for x in range(2, 27) if x % 2 == 0]
print(ans)
```

## Task

 N_3

```python
ans = [i for i in range(1, 1000) if str(i) == str(i)[::-1]]
print(ans)
```

## Task

 N_15

```python
import json

input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""

d = {x.split(",")[0]: x.split(",")[1:] for x in input_str.split()}
print(json.dumps([{j: d[j][k] for j in d.keys()} for k in range(len(d.keys()))], indent=2))

```
