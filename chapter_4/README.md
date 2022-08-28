## ex_4-1
```
pizzas = ['carbonara', 'peperoni', 'bbq']
for pizza in pizzas:
    print('I like ' + pizza + ' pizza.')
print('I really love pizza!')
```

```
PS D:\python-crash-course-2022> python chapter_4/ex_4-1.py
I like carbonara pizza.
I like peperoni pizza.
I like bbq pizza.
I really love pizza!
```
***
## ex_4-2
```
pets = ['cat', 'dog', 'rabbit']
for pet in pets:
    print(pet.title() + ' can scatter wool around the apartment.')
print('\n' + 'Each of them can be a best friend.')
```

```
PS D:\python-crash-course-2022>  python chapter_4/ex_4-2.py
Cat can scatter wool around the apartment.
Dog can scatter wool around the apartment.
Rabbit can scatter wool around the apartment.

Each of them can be a best friend.
```
***
## ex_4-3
```
for value in range(1,21):
    print(value) 
```

```
PS D:\python-crash-course-2022> python chapter_4/ex_4-3.py                                 
1
2    
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```

***
## ex_4-4
```
numbers = []
for number in range(0,1000000):
    number=number+1
    numbers.append(number)
print(numbers)
```

***
## ex_4-5
```
numbers = []
for number in range(0,1000000):
    number=number+1
    numbers.append(number)

min = min(numbers)
max = max(numbers)
suma = sum(numbers)
print(min)
print(max)
print(suma)
```

```
PS D:\python-crash-course-2022> python chapter_4/ex_4-5.py
1
1000000
500000500000
```

***
## ex_4-6
```
for value in range(1,21,2):
    print(value)

```

```
PS D:\python-crash-course-2022> python chapter_4/ex_4-6.py
1
3
5
7
9
11
13
15
17
19
```

***
## ex_4-7
```
for value in range(0,30,3):
    print(value)

```

```
PS D:\python-crash-course-2022> python chapter_4/ex_4-7.py
0
3
6
9
12
15
18
21
24
27
```

***
## ex_4-8
```
cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)

print(cubes)
```

```
PS D:\python-crash-course-2022> python chapter_4/ex_4-8.py
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

***
## ex_4-9
```
cubes = [value**3 for value in range(1,11)]
print(cubes)
```

```
PS D:\python-crash-course-2022>  python chapter_4/ex_4-9.py
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

***
## ex_4-10
