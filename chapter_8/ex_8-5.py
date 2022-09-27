def describe_city(city, country='ukraine'):
    """Друк міста і країни (по замовчуванню, якщо не вказано додатково)"""
    print(f'{city.title()} is in {country.title()}.')
    
describe_city('kyiv')
describe_city('kharkiv')
describe_city('lviv')
describe_city('oslo', country='norway')
describe_city('warsaw', 'poland')