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
print(f'Dear, {friends[0].title()}, I will be glad to see you at dinner.')
print(f'Dear, {friends[1].title()}, I will be glad to see you at dinner.')
print(f'Dear, {friends[2].title()}, I will be glad to see you at dinner.')
print(f'Dear, {friends[3].title()}, I will be glad to see you at dinner.')
print(f'Dear, {friends[4].title()}, I will be glad to see you at dinner.')