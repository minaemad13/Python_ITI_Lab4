class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def eat(self, meals):
        meals = int(meals)
        if meals == 3:
            return "100% hth"
        elif meals == 2:
            return "75% hth"
        elif meals == 1:
            return "50% hth"
        elif meals == 0:
            return "0% hth"
        elif meals > 3:
            return "fat"
        else:
            return "wrong input"

    def sleep(self, hours):
        hours = int(hours)
        if hours == 7:
            return "Happy"
        elif hours < 7:
            return "tired"
        else:
            return "Lazy"

    def buy(self, items):
        items = int(items)
        self.money += items * 10
        return self.money

    @property  # print property value
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self, helth):
        if helth >= 0 and helth <= 100:
            self.__healthRate = helth
        else:
            print("must be between 0 to 100.")
