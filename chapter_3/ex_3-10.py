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


