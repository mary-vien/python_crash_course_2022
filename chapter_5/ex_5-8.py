users = ['admin', 'mary', 'cary', 'mariia',
          'vasyl', 'marko', 'ivan']
for user in users:
    if user == 'admin':
        print(f'Hello {user}, would you like to see a status report?')
    else:
        print(f'Hello {user.title()}, thank you for logging in again!')
