"""Preconditions:
1. Створити клас Human, в якому визначити метод drink.
При ініціалізації, приймати вік людини; створити поле класу favorite_drink зі значенням 'beer'.
2. Створити клас Worker, віднаслідувавши його від Human, та додавши при ініціалізації зарплату."""

"""Завдання:
1. Реалізувати метод drink, так щоб він виводив в консоль назву поточного класу
та додавав до неї відповідну дію та напій;
Якщо людині менше 18 років, заміняти улюблений напій на 'juice'

1.1. Використовуючи даний клас, зробити виклик який:
а) Виведе в консоль улюблений напій людини
б) Виведе в консоль всю фразу, наприклад "Human likes drink beer"
якщо людині більше 18 років, та "Human likes drink juice" якщо ні."""


class Human:
    favorite_drink = 'beer'

    def __init__(self, human_age):
        self.age = human_age
        if human_age < 18:
            self.favorite_drink = 'juice'
            print('Human likes drink ' + self.favorite_drink)
        else:
            print('Human likes drink ' + self.favorite_drink)

    def drink(self):
        print(self.favorite_drink)


human1 = Human(18)
human2 = Human(17)

"""console answers
Human likes drink beer
Human likes drink juice"""


class Worker(Human):
    """2. Перевизначити в класі Worker улюблений напій таким чином,
щоб коли зарплата людини більша за 1000, то він змінювався на 'whiskey'
Вивести в консоль все так само як в першому завданні, але з урахуванням зарплати."""

    def __init__(self, human_age, worker_salary):
        self.age = human_age
        self.salary = worker_salary
        if human_age < 18:
            self.favorite_drink = 'juice'
            print('Human likes drink ' + self.favorite_drink)
        elif worker_salary > 1000:
            self.favorite_drink = 'whiskey'
            print('Human likes drink ' + self.favorite_drink)
        else:
            print('Human likes drink ' + self.favorite_drink)


worker1 = Worker(17, 1000)
worker2 = Worker(23, 1200)
worker3 = Worker(22, 1000)


"""console answers
Human likes drink juice
Human likes drink whiskey
Human likes drink beer"""
