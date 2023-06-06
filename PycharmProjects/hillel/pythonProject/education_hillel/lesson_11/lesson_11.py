class Human:
    default_name = "Julia Rodenkova"
    default_age = 33

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Bank account: {self.__money}")
        print(f"House: {self.__house}")

    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}")
        print(f"Default age: {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount

    def buy_house(self, house, discount=0):
        final_price = house.final_price(discount)
        if self.__money >= final_price:
            self.__make_deal(house, final_price)
            print(f"Congratulations! {self.name} bought a house.")
        else:
            print(f"Sorry, {self.name} should work harder to buy the house.")


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price - discount

    def __str__(self):
        return f"House: {self.__class__.__name__} (Area: {self._area}m², Price: {self._price})"


class SmallHouse(House):
    def __init__(self):
        super().__init__(40, 30000)


Human.default_info()

human = Human()
human.info()

house = SmallHouse()

buy_house_decision = input("Do you want to buy a house? (yes/no): ")
if buy_house_decision.lower() == "yes":
    earnings = int(input("How much money does Julia Rodenkova earn? "))
    human.earn_money(earnings)

    apply_discount = input("Will Julia flirt with the manager to get a discount? (yes/no): ")
    if apply_discount.lower() == "yes":
        discount = int(input("Enter the discount amount: "))
        human.buy_house(house, discount)
    else:
        human.buy_house(house)

    human.info()
else:
    print("Poor thing!")
