## ex_3-1
```
names = ['Vasyl', 'Mariia', 'Cary', 'Mary']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
```

```
names = ['Vasyl', 'Mariia', 'Cary', 'Mary']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
```

***
## ex_3-2
```
names = ['vasyl', 'mariia', 'cary', 'mary']
message_0 = 'В квартирі №38 живе ' + names[0].title() + '.'
message_1 = 'В квартирі №38 живе ' + names[1].title() + '.'
message_2 = 'В квартирі №38 живе ' + names[2].title() + '.'
message_3 = 'В квартирі №38 живе ' + names[3].title() + '.'
print(message_0)
print(message_1)
print(message_2)
print(message_3)
```

```
PS D:\python-crash-course-2022> python chapter_3/ex_3-2.py
В квартирі №38 живе Vasyl.
В квартирі №38 живе Mariia.
В квартирі №38 живе Cary.
В квартирі №38 живе Mary.
```

***
## ex_3-3
```
transport = ['ford mustang', 'volkswagen golf', 'метро', 'ardis']
message_0 = 'В дитинстві я хотіла собі ' + transport[0].title() + '.'
message_1 = 'Ставши дорослою я зрозуміла, що більш практичнішим є ' + transport[1].title() + '.'
message_2 = 'Зараз я катаюсь на ' + transport[2] + '.'
message_3 = 'А з транспорту в мене власний лиш ' + transport[3].title() + '. Але він велосипед і на ньому далеко не заїдеш.'
print(message_0 + '\n' + message_1 + '\n' + message_2 + '\n' + message_3)
```

```
PS D:\python-crash-course-2022> python chapter_3/ex_3-3.py
В дитинстві я хотіла собі Ford Mustang.
Ставши дорослою я зрозуміла, що більш практичнішим є Volkswagen Golf.
Зараз я катаюсь на метро.
А з транспорту в мене власний лиш Ardis. Але він велосипед і на ньому далеко не заїдеш.
```

##
ex_3-4
```
friends = ['monica', 'phebe', 'rachel']
print('Dear, ' + friends[0].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[1].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[2].title() + ', I will be glad to see you at dinner.')
```

```
PS D:\python-crash-course-2022> python chapter_3/ex_3-4.py
Dear, Monica, I will be glad to see you at dinner.
Dear, Phebe, I will be glad to see you at dinner.
Dear, Rachel, I will be glad to see you at dinner.
```

***
## ex_3-5
```
friends = ['monica', 'phebe', 'rachel']
print('Dear, ' + friends[0].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[1].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[2].title() + ', I will be glad to see you at dinner.')

print('\n')
print(friends[1].title() + ' will be absent.')
friends[1] = 'janice'
print('\n')
print('Dear, ' + friends[0].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[1].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[2].title() + ', I will be glad to see you at dinner.')
```

```
PS D:\python-crash-course-2022> python chapter_3/ex_3-5.py
Dear, Monica, I will be glad to see you at dinner.
Dear, Phebe, I will be glad to see you at dinner.
Dear, Rachel, I will be glad to see you at dinner.


Phebe will be absent.


Dear, Monica, I will be glad to see you at dinner.
Dear, Janice, I will be glad to see you at dinner.
Dear, Rachel, I will be glad to see you at dinner.
```
***
## ex_3-6
```
friends = ['monica', 'phebe', 'rachel']
print('Dear, ' + friends[0].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[1].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[2].title() + ', I will be glad to see you at dinner.')
print('\n')
print(friends[1].title() + ' will be absent.')
print("Let's invite Janice")
friends[1] = 'janice'
print("The guest list will be increased. Let's invite the boys")
friends.insert(0, 'ross')
friends.insert(2, 'chandler')
friends.append('joey')
print(friends)
print('\n')
print('Dear, ' + friends[0].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[1].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[2].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[3].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[4].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[5].title() + ', I will be glad to see you at dinner.')

```

```
PS D:\python-crash-course-2022> python chapter_3/ex_3-6.py
Dear, Monica, I will be glad to see you at dinner.
Dear, Phebe, I will be glad to see you at dinner.
Dear, Rachel, I will be glad to see you at dinner.


Phebe will be absent.
Let's invite Janice
The guest list will be increased. Let's invite the boys
['ross', 'monica', 'chandler', 'janice', 'rachel', 'joey']


Dear, Ross, I will be glad to see you at dinner.
Dear, Monica, I will be glad to see you at dinner.
Dear, Chandler, I will be glad to see you at dinner.
Dear, Janice, I will be glad to see you at dinner.
Dear, Rachel, I will be glad to see you at dinner.
Dear, Joey, I will be glad to see you at dinner.
```
***
## ex_3-7
```
friends = ['monica', 'phebe', 'rachel']
print('Dear, ' + friends[0].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[1].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[2].title() + ', I will be glad to see you at dinner.')
print('\n')
print(friends[1].title() + ' will be absent.')
print("Let's invite Janice")
friends[1] = 'janice'
print("The guest list will be increased. Let's invite the boys")
friends.insert(0, 'ross')
friends.insert(2, 'chandler')
friends.append('joey')
print(friends)
print('\n')
print('Dear, ' + friends[0].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[1].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[2].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[3].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[4].title() + ', I will be glad to see you at dinner.')
print('Dear, ' + friends[5].title() + ', I will be glad to see you at dinner.')

print('Forced to invite only two friends. Unfortunately.' + '\n')
del1_friends = friends.pop(0)
print('Sorry, ' + del1_friends.title() + ' unfortunately you are not invited.')

## для розуміння хто зараз залишився
print(friends)

del2_friends = friends.pop(1)
print('Sorry, ' + del2_friends.title() + ' unfortunately you are not invited.')

## для розуміння хто зараз залишився
print(friends)

del3_friends = friends.pop(3)
print('Sorry, ' + del3_friends.title() + ' unfortunately you are not invited.')

## для розуміння хто зараз залишився
print(friends)

del4_friends = friends.pop(1)
print('Sorry, ' + del3_friends.title() + ' unfortunately you are not invited.')

## для розуміння хто зараз залишився
print(friends)
print('\n')


print('Dear, ' + friends[0].title() + ', I will be glad to see you at dinner. The decision is final.')
print('Dear, ' + friends[1].title() + ', I will be glad to see you at dinner. The decision is final.')

del friends[0]
del friends[0]
print(friends)
```

```
PS D:\python-crash-course-2022> python chapter_3/ex_3-7.py
Dear, Monica, I will be glad to see you at dinner.
Dear, Phebe, I will be glad to see you at dinner.
Dear, Rachel, I will be glad to see you at dinner.


Phebe will be absent.
Let's invite Janice
The guest list will be increased. Let's invite the boys
['ross', 'monica', 'chandler', 'janice', 'rachel', 'joey']


Dear, Ross, I will be glad to see you at dinner.
Dear, Monica, I will be glad to see you at dinner.
Dear, Chandler, I will be glad to see you at dinner.
Dear, Janice, I will be glad to see you at dinner.
Dear, Rachel, I will be glad to see you at dinner.
Dear, Joey, I will be glad to see you at dinner.
Forced to invite only two friends. Unfortunately.

Sorry, Ross unfortunately you are not invited.
['monica', 'chandler', 'janice', 'rachel', 'joey']
Sorry, Chandler unfortunately you are not invited.
['monica', 'janice', 'rachel', 'joey']
Sorry, Joey unfortunately you are not invited.
['monica', 'janice', 'rachel']
Sorry, Joey unfortunately you are not invited.
['monica', 'rachel']


Dear, Monica, I will be glad to see you at dinner. The decision is final.
Dear, Rachel, I will be glad to see you at dinner. The decision is final.
[]
```
***
## ex_3-8
```
countries = ['ukraine', 'netherlands', 'france', 'belgium', 'georgia']
print('\n')

print('Початковий перелік країн: ')
print(countries)
print('\n')

print('Відсортований перелік по алфавіту: ')
print(sorted(countries))
print('\n')

print('Перевірка чи список зберігся: ')
print(countries)
print('\n')

print('Перелік в зворотньому алфавітному порядку: ')
print(sorted(countries, reverse=True))
print('\n')

print('Перевірка чи список зберігся: ')
print(countries)
print('\n')

print('Змінюю перелік, має друкуватись з зворотньому порядку: ')
countries.reverse()
print(countries)
print('\n')

print('Змінюю перелік вдруге, має бути як на початку: ')
countries.reverse()
print(countries)
print('\n')

countries.sort()
print('Змінила перелік командою sort, перевірка: ')
print(countries)
print('\n')

countries.sort(reverse=True)
print('Перелік в зворотньому алфавітному порядку: ')
print(countries)


print('\n')
```

```
python chapter_3/ex_3-8.py


Початковий перелік країн:
['ukraine', 'netherlands', 'france', 'belgium', 'georgia']


Відсортований перелік по алфавіту:
['belgium', 'france', 'georgia', 'netherlands', 'ukraine']


Перевірка чи список зберігся:
['ukraine', 'netherlands', 'france', 'belgium', 'georgia']


Перелік в зворотньому алфавітному порядку:
['ukraine', 'netherlands', 'georgia', 'france', 'belgium']


Перевірка чи список зберігся:
['ukraine', 'netherlands', 'france', 'belgium', 'georgia']


Змінюю перелік, має друкуватись з зворотньому порядку:
['georgia', 'belgium', 'france', 'netherlands', 'ukraine']


Змінюю перелік вдруге, має бути як на початку:
['ukraine', 'netherlands', 'france', 'belgium', 'georgia']


Змінила перелік командою sort, первірка:
['belgium', 'france', 'georgia', 'netherlands', 'ukraine']


Перелік в зворотньому алфавітному порядку:
['ukraine', 'netherlands', 'georgia', 'france', 'belgium']

```
***
## ex_3-9
```
friends = ['monica', 'phebe', 'rachel']
sum = len(friends)
print(sum)
```

```
PS D:\python-crash-course-2022> python chapter_3/ex_3-9.py
3
```
***
## ex_3-10
```
print('Add list: ')
mountains = ['hoverla', 'brebeneskul', 'pip ivan chornohora', 'petros', 'hutyn tomnatyk', 'rebra', 'menchul', 'pip ivan', 'turkul', 'breskul']
print(mountains)
print('\n' + 'друкую деякі назви з переліку:')
print(mountains[5].title())
print(mountains[0].title())
message = 'Найвищою вершиною України є ' + mountains[0].title() + '.'

print('\n' + 'замінюю перший пункт на:')
mountains[0]='everest'
print(mountains[0].title())
print(mountains)

print('\n' + 'замінюю перший пункт на: ')
mountains[0]='hoverla'
print(mountains[0].title())
print(mountains)

print('\n' + 'додаю назву smotrych, показую список: ')
mountains.append('smotrych')
print(mountains)

print('\n' + 'дивлюсь як називається пункт 5 і видаляю його, потім показую як змінився перелік: ')
print(mountains[5].title())
del mountains[5]
print(mountains)

print('\n' + 'додаю пунктом 5 назву rebra, друкую список:  ')
mountains.insert(5, 'rebra')
print(mountains)

print('\n' + 'видаляю пункти 3,5,7, показую список без них, показую ивдалені елементи: ')
popped_mountains = mountains.pop(3) + ', ' + mountains.pop(5) + ', ' + mountains.pop(7)
print(mountains)
print(popped_mountains)

print('\n' + 'видаляю зі списку назву turkul, показую список: ')
mountains.remove('turkul')
print(mountains)

print('\n' + 'сортую (тимчасово) перелік: ')
print(sorted(mountains))
print('\n' + 'перевіряю чи все залишилось на місці: ')
print(mountains)

print('\n' + 'перелік (тимчасовий) в зворотньому порядку, потім перевірка постійного:')
print(sorted(mountains, reverse=True))
print('\n' + 'перевіряю чи все залишилось на місці: ')
print(mountains)

print('\n' + 'перелік в зворотньому порядку: ')
mountains.reverse()
print(mountains)

print('\n' + 'сортую назавжди, перевірка: ')
mountains.sort()
print(mountains)

print('\n' + 'визначаю довжину списку: ')
length = len(mountains)
print(length)

print('\n')
```

```
python chapter_3/ex_3-10.py
Add list: 
['hoverla', 'brebeneskul', 'pip ivan chornohora', 'petros', 'hutyn tomnatyk', 'rebra', 'menchul', 'pip ivan', 'turkul', 'breskul']

друкую деякі назви з переліку:
Rebra
Hoverla

замінюю перший пункт на:
Everest
['everest', 'brebeneskul', 'pip ivan chornohora', 'petros', 'hutyn tomnatyk', 'rebra', 'menchul', 'pip ivan', 'turkul', 'breskul']

замінюю перший пункт на:
Hoverla
['hoverla', 'brebeneskul', 'pip ivan chornohora', 'petros', 'hutyn tomnatyk', 'rebra', 'menchul', 'pip ivan', 'turkul', 'breskul']

додаю назву smotrych, показую список:
['hoverla', 'brebeneskul', 'pip ivan chornohora', 'petros', 'hutyn tomnatyk', 'rebra', 'menchul', 'pip ivan', 'turkul', 'breskul', 'smotrych']

дивлюсь як називається пункт 5 і видаляю його, потім показую як змінився перелік:
Rebra
['hoverla', 'brebeneskul', 'pip ivan chornohora', 'petros', 'hutyn tomnatyk', 'menchul', 'pip ivan', 'turkul', 'breskul', 'smotrych']

додаю пунктом 5 назву rebra, друкую список:
['hoverla', 'brebeneskul', 'pip ivan chornohora', 'petros', 'hutyn tomnatyk', 'rebra', 'menchul', 'pip ivan', 'turkul', 'breskul', 'smotrych']

видаляю пункти 3,5,7, показую список без них, показую ивдалені елементи:
['hoverla', 'brebeneskul', 'pip ivan chornohora', 'hutyn tomnatyk', 'rebra', 'pip ivan', 'turkul', 'smotrych']
petros, menchul, breskul

видаляю зі списку назву turkul, показую список:
['hoverla', 'brebeneskul', 'pip ivan chornohora', 'hutyn tomnatyk', 'rebra', 'pip ivan', 'smotrych']

сортую (тимчасово) перелік:
['brebeneskul', 'hoverla', 'hutyn tomnatyk', 'pip ivan', 'pip ivan chornohora', 'rebra', 'smotrych']

перевіряю чи все залишилось на місці:
['hoverla', 'brebeneskul', 'pip ivan chornohora', 'hutyn tomnatyk', 'rebra', 'pip ivan', 'smotrych']

перелік (тимчасовий) в зворотньому порядку, потім перевірка постійного:
['smotrych', 'rebra', 'pip ivan chornohora', 'pip ivan', 'hutyn tomnatyk', 'hoverla', 'brebeneskul']

перевіряю чи все залишилось на місці:
['hoverla', 'brebeneskul', 'pip ivan chornohora', 'hutyn tomnatyk', 'rebra', 'pip ivan', 'smotrych']

перелік в зворотньому порядку:
['smotrych', 'pip ivan', 'rebra', 'hutyn tomnatyk', 'pip ivan chornohora', 'brebeneskul', 'hoverla']

сортую назавжди, перевірка:
['brebeneskul', 'hoverla', 'hutyn tomnatyk', 'pip ivan', 'pip ivan chornohora', 'rebra', 'smotrych']

визначаю довжину списку:
7

```




