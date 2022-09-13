favorite_languages = {
                    'jen': 'python', 
                    'sarah': 'c', 
                    'edward': 'ruby', 
                    'phil': 'python',
                    }

friends = ['jen', 'sarah', 'mathew', 'arthur', 'edward', 'phil', 'max']

for friend in friends:
    if friend in favorite_languages.keys():
        print(f"Hi, {friend.title()}. Thank you for participating in the survey.")
    else:
        print(f'{friend.title()}, please take part in the survey.')