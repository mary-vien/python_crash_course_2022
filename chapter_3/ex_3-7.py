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