def make_shirt(size='L', text='I love Python'):
    """Друк тексту із розміром і написом (обидва варіанти по замовчуванню, якщо не вказано інакше)"""
    print(f'\nSize t-shirt: {size}. \nText on t-shirt: "{text}".')

make_shirt()
make_shirt(size='M', text='Python is cool!')