# Lists
'''
1. Упорядоченные списки (НЕ тоже самое что и сортировка)
2. Динамические
3. 

l = [1,22, 'banana', 'cat', 3.14159]

l += ['Odesa', 'Kyiv', ]

l.append(['Kharkiv', 'Lviv']) # Добавляет в конец списка еще один список
l.insert(2, 'Apple') # Добавляет в список элемент на позицию 2
l.remove('banana')  # Удаляет из списка элемент 'banana'
l.pop(4) # Удаляет элемент с позиции, если нет параметра - последний


print(l.count('cat'))
cities=['New York', 'Chicago', 'Detroit']
cities.sort()
print(cities)

n = [1, 2, [10, 20, 30], [40, 50, 60], 3, 4, 5]

n[2].insert(1, [15,16,17,18])
print(n[2][1][-2])
'''

t = (1, 2, 3)