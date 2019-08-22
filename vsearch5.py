# Возврат более одного значения
def search4vowels(word: str) -> set:  # в аргументе 'word' ожидается строка, функция возвращает множество
    """Возвращает гласные, найденные в указанном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))  # возврат данных без использования переменной 'found'


print(search4vowels('hello world'))
