def make_car(producer, model, **info):
    """Будує словник з інформацією про авто."""
    profile = {}
    profile['producer'] = producer
    profile['model_name'] = model
    for key, value in info.items():
        profile[key] = value
    return profile

car = make_car('volkswagen', 'passat',
                            color = 'blue',
                            year = 2012,
                            engine_capacity = 2.5,
                            fuel = ['gasoline', 'gas']
                            )
print(car)

