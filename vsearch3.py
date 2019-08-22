# Возврат более одного значения
def search4vowels(word):
    """Возвращает гласные, найденные в указанном слове."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return found  # возврат значений в виде структуры данных (множества)


print(search4vowels('hello world'))
