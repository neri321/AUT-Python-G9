"""Домашнє завдання №4: Послідовності та колекції

a) List (список)
Preconditions:
    Створити список міст України, наприклад: Львів, Київ, Одеса, Дніпро, Суми
    Створити список з міст, які Ви вже колись відвідали, наприклад Київ, Львів
Завдання:
    Пройтись по списку відвіданих міст, вилучити поточне місто з першого списку,
    надрукувати його в консоль.
Очікуваний результат:
    В першому списку міст залишились тільки ті міста, які Ви ще не відвідали."""

cities = ['Львів', 'Київ', 'Одеса', 'Дніпро', 'Суми', 'Харків', 'Донецьк', 'Полтава', 'Чернівці', 'Ужгород']
visited_cities = ['Львів', 'Київ', 'Одеса', 'Харків', 'Полтава']
not_visited_cities = [city for city in cities if city not in visited_cities]

print(not_visited_cities)

"""b) Tuple (кортеж)
Preconditions:
    Створити кортеж елементів, наприклад 3, 'one', 2.25
Завдання:
    1. Вивести в консоль всі об'єкти кортежу циклом
    2. Спробувати змінити елемент кортежу в індексі 0 (очікуємо помилку)
    3. Знайти спосіб змінити кортеж так, щоб першим елементом стало число збільшене на 2
       (підказка: можна використати кастинг (приведення до певного типу))"""

tpl = (3, 'one', 2.25, 4, 'two', 2.26)

for item in tpl:
    print(item)

lst = list(tpl)
lst[0] *= 2
print(tuple(lst))

"""с) String (Рядок)
Preconditions:
    Створити будь-який рядок українською мовою, маленькими літерами, що міститиме
    кілька голосних літер
Завдання:
    Використовуючи list comprehension та join відтворити цей рядок таким чином,
    щоб всі голосні літери стали великими"""
# the first try
doc = 'мені дуже подобається вивчати пайтон! здається, це найлегша з потужних мов для вивчення.'


# def upper_vowels(text: str):
#     vowels_letter = 'аоиіуєеяюї'
#     for letter in text:
#         if letter in vowels_letter:
#             text = text.replace(letter, letter.upper())
#     return text
#
#
# print(upper_vowels(doc))

# the second try
vowel_letters = 'аоиіуєеяюї'
lst = ''.join([x.upper() if x in vowel_letters else x for x in doc])  # list comprehension
print(lst)

"""d) Set (Множина)
Preconditions:
    Створити список з кількох літер, деякі з яких повторюються та є голосні літери
Завдання:
    Перетворити цей список на множину, з заміною малих голосних літер на великі"""

list_of_letter = ['a', 'a', 'b', 'c', 'c', 'd', 'e', 'e', 'f', 'f', 'g', 'h', 'i']

vowels = ['a', 'e', 'i', 'o', 'u']
set_of_list = set([x.upper() if x in vowels else x for x in list_of_letter])  # list comprehension

print(list_of_letter)
print(set_of_list)

"""e) Dictionary (Словник)
Preconditions:
    Створити 2 списки: [1, 2, 3] та ['one', 'two', 'three']
Завдання:
    1. Перетворити ці 2 списки на словник, де ключами буде перший список, а значеннями -- другий
    2. В словнику що утворився, поміняти місцями ключі та значення
    3. Погуглити, почитати і запам'ятати які об'єкти можуть виступати ключами в словнику
       та спробувати зрозуміти чому це так"""

lst_of_keys = [1, 2, 3, 4, 5]
lst_of_values = ['one', 'two', 'three', 'four', 'five']

res = dict(zip(lst_of_keys, lst_of_values))
res1 = {
    value: key
    for key, value
    in res.items()
}
print(res)
print(res1)
