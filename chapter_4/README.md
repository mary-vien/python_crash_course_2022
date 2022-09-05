# Chapter_4

## ex_4-1
```python
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
```python
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
```python
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
```python
numbers = []
for number in range(0,1000000):
    number=number+1
    numbers.append(number)
print(numbers)
```

***
## ex_4-5
```python
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
```python
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
```python
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
```python
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
```python
cubes = [value**3 for value in range(1,11)]
print(cubes)
```

```
PS D:\python-crash-course-2022>  python chapter_4/ex_4-9.py
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

***
```python
friends = ['monica', 'phebe', 'rachel', 'ross', 'chandler', 'joey']
## зріз позначається через індекси
print(friends[0:3]) ##друкуються елементи від 0 до 2 включно
print(friends[1:4]) ##друкуються елементи від 1 до 3 включно
print(friends[3:]) ##друкуються від 3 до останнього 
print(friends[-3:]) ##друкуються 3 останні
print(friends[:3]) ##друкуються елементи від 0 до 2 включно. якщо не вказано початок зрізу, то автоматично береться 0


print('Friends: ')
for friend in friends[:3]:
    print(friend.title())

print(friends[:]) ##друкується весь список
```
***
## ex_4-10
```python
friends = ['monica', 'phebe', 'rachel', 'ross', 'chandler', 'janice', 'joey']
print(friends[:])
print(f'список перших трьох людей:  {friends[:3]}')
print(f'список трьох людей посередині:  {friends[2:5]}')
print(f'список останніх трьох людей:  {friends[-3:]}')

```

```
PS D:\python-crash-course-2022> python chapter_4/ex_4-10.py
['monica', 'phebe', 'rachel', 'ross', 'chandler', 'janice', 'joey']
список перших трьох людей:  ['monica', 'phebe', 'rachel']
список трьох людей посередині:  ['rachel', 'ross', 'chandler']
список останніх трьох людей:  ['chandler', 'janice', 'joey']
```
## ex_4-13
```python
pizzas = ['carbonara', 'peperoni', 'bbq']
friend_pizzas = pizzas[:]

pizzas.append('marharyta')
friend_pizzas.append('hawaii')

print('\nMy favorite pizza are: ')
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizza are: ")
for pizza in friend_pizzas:
    print(pizza.title())  
```

```
PS D:\python-crash-course-2022> python chapter_4/ex_4-11.py

My favorite pizza are:
Carbonara
Peperoni
Bbq
Marharyta

My friend's favorite pizza are:
Carbonara
Peperoni
Bbq
Hawaii
```
***
## ex_4-12
```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('canolli')
friends_foods.append('ice cream')
print('\n')
for food in my_foods:
    print(f'My food: {food.title()}')
print('\n')
for food in friends_foods:
    print(f'Friend`s food: {food.title()}')
```

```
PS D:\python-crash-course-2022> python chapter_4/ex_4-12.py


My food: Pizza
My food: Falafel
My food: Carrot Cake
My food: Canolli


Friend`s food: Pizza
Friend`s food: Falafel
Friend`s food: Carrot Cake
Friend`s food: Ice Cream
```

***
## ex_4-13
```python
print('Original menu: ')
foods = ('scrambled eggs', 'salmon', 'oatmeal', 'orange juice', 'coffee')
for food in foods:
    print(food.title())

print('\nModified menu: ')
foods = ('pasta', 'salmon', 'oatmeal', 'orange juice', 'tea')
for food in foods:
    print(food.title())
```

```
PS D:\python-crash-course-2022>  python chapter_4/ex_4-13.py
Original menu: 
Scrambled Eggs
Salmon
Oatmeal
Orange Juice
Coffee

Modified menu:
Pasta
Salmon
Oatmeal
Orange Juice
Tea
```
***
