current_users = ['mary', 'cary', 'mariia',
                'vasyl', 'matvii', 'Ivan']
new_users = ['iryna', 'matvii', 'IVAN', 'arthur', 'anna']


for new_user in new_users:
    if new_user.lower() in list(map(lambda x: x.lower(), current_users)): 
        print(f'Username {new_user} not available. Choose a new username')
    else:
        print(f'Username {new_user} is available')
