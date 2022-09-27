def build_profile(first, last, **user_info):
    """Будує словник з інформацією про користувача."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('mariia', 'popach',
                            location='kyiv',
                            pets = ['mary', 'cary'],
                            age = 25,
                            hobby = ['climbing', 'plants', 'hiking'],
                            )
print(user_profile)