# Возврат одного значения
def search4vowels(word):
    """Возвращает булево значение в зависимости от присутствия любых гласных."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)  # передача имени структуры данных, которая содержит результат поиска гласных


print(search4vowels('hello world'))
