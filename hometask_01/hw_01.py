"""1. Створити список з 3-4 елементів, вивести суму всіх його елементів
    (це можуть бути цифри або рядки, головне щоб усе одного типу)"""

lst = ['John', 'Sarah', 'Bob', 'Gloria']
print(' '.join(lst))

"""2. Створити список з 5-6 елементів, деякі з яких повторюються. Вивести суму унікальних значень."""

lst = [8, 9, 9, 10, 11, 11]
st = set(lst)
print(sum(st))

"""3. Створити словник де є поле "зарплата". Перевизначити значення цього поля,
    щоб воно дорівнювало 1.5 від початкової зарплати."""

dct = {'first_name': 'John','surname': 'Smith','salary': 1000}
dct['salary'] *= 1.5
print(dct)
