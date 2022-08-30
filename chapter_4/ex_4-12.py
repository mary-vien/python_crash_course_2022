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
