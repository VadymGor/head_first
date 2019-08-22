# Принимает любое множество букв и ищет их в указанной фразе
def search4letters(phrase: str, letters: str) -> set:
    """Возвращает множество букв из 'letters', найденных в указанной фразе."""
    return set(letters).intersection(set(phrase))  # находит пересечение множества, созданного из 'letters',
    # с множеством, созданным из 'phrase'


print(search4letters("hello world", 'lh'))
