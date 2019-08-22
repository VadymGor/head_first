# Возврат более одного значения
def search4vowels(word):
    """Возвращает гласные, найденные в указанном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))  # возврат данных без использования переменной 'found'


print(search4vowels('hello world'))
