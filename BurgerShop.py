# Author: Obed Gyawu
# Date: July 13, 2022


class FoodItem:

    def __init__(self, kind, cost):
        self.kind = kind
        self.cost = cost

    def __str__(self):
        return "items: " + self.kind + "\n" + "cost: $" + str(self.cost) + "\n"

    def get_cost(self):
        return self.cost


class Burger(FoodItem):

    def __init__(self, kind, cost):
        super(Burger, self).__init__(kind, cost)
        self.condiments = []

    def add_condiment(self, condiment):
        if condiment not in self.condiments:
            self.condiments.append(condiment)

    def __str__(self):
        a = super(Burger, self).__str__()
        a = a + "condiment: " + ", ".join(self.condiments)
        return a


class Drink(FoodItem):
    def __init__(self, kind, size, cost):
        super(Drink, self).__init__(kind, cost)
        self.size = size

    def __str__(self):
        a = super(Drink, self).__str__()
        a = a + "size: " + str(self.size)
        return a


class Side(FoodItem):
    def __init__(self, kind, cost):
        super(Side, self).__init__(kind, cost)


class Combo(FoodItem):
    def __init__(self, kind, k, p, a, discount):
        self.kind = kind
        self.Burger = k
        self.Drink = p
        self.Side = a
        self.discount = discount
        self.cost = self.Burger.get_cost() + self.Drink.get_cost() + self.Side.get_cost() - self.discount

    def __str__(self):
        a = ""
        a = a + "combo: " + self.kind + "\n"
        a = a + str(self.Burger) + "\n" + str(self.Drink) + "\n" + str(self.Side) + "\n"
        a = a + "Cost of combo before discount: $" + str(self.Burger.get_cost() + self.Drink.get_cost() + self.Side.get_cost()) + "\n"

        a = a + "discount: $" + str(self.discount) + "\n"
        a = a + "cost of combo after discount: $" + str(self.cost) + "\n"

        return a


class Order:
    def __init__(self, kind):
        self.kind = kind
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_cost(self):
        cost = 0.0
        for item in self.items:
            cost = cost + item.get_cost()
        return cost

    def __str__(self):
        s = [str(item) for item in self.items]
        return "\n".join(s)

    def display(self):
        print("--------------------------------")
        print("Here is a summary of your order")
        print("order for " + self.kind)
        print("list of items in the order")

        for item in self.items:
            print("-----------")
            print(str(item))
        print("-----------")
        print("Your order total amount is :$" + str(self.get_cost()))
        print("==========================================")


cost_of_burger = 5.00
condiments_for_burger = ["onion", "lettuce", "cheese", "tomatoes"]

types_of_drink = ["lemonade", "pepsi", "fruit punch"]
size_of_drink = ["small", "medium", "large"]
cost_of_drink = [3.00, 4.00, 5.00]

cost_of_size = 4.00
sides_for_combo = ["fries", "hash-browns", "salad"]

discount_for_combo = 3.00


def get_burger():
    k = Burger("Burger", cost_of_burger)
    f1 = input("Do you like to add any condiments for your burger? (y for yes) ")
    if f1.lower() == "y":
        for condiment in condiments_for_burger:
            f = input("Do you like " + str(condiment) + "? (y/n): ")
            if f.lower() == "y":
                k.add_condiment(condiment)
    return k


def get_drink():
    print("Here are the  drinks we have:")
    print(types_of_drink)
    print("Here are the sizes of drink we have:")
    print(size_of_drink)
    choice = False
    drink_name = None
    drink_size = None
    drink_cost = None
    while choice == False:
        f1 = input("What do you like to drink? ")
        if f1.lower() in types_of_drink:
            choice = True
            drink_name = f1.lower()
        else:
            print("Please enter a valid drink.")
    choice = False
    while choice == False:
        f1 = input("What drink size you want? " + str(size_of_drink) + ": ")
        if str(f1) in size_of_drink:
            choice = True
            drink_size = str(f1)
        else:
            print("please enter a valid size")
    # locate the price of the drink based on the index of the size:
    drink_cost = cost_of_drink[size_of_drink.index(drink_size)]
    p = Drink(drink_name, drink_size, drink_cost)

    # ask user for input and store it in drink object
    return p


def get_side():
    print("These are the available sides:")
    print(sides_for_combo)
    choice = False
    side_name = None
    while choice == False:
        f1 = input("What side do you want? ")
        if f1.lower() in sides_for_combo:
            choice = True
            side_name = f1.lower()
        else:
            print("Please enter a valid side.")
    a = Side(side_name, cost_of_size)

    # ask user for input and store it in side object
    return a


def get_combo():
    print("Let's get you a combo meal!")
    print("First, let's order the burger for your combo.")
    k = get_burger()
    print("Now, let's order the drink for your combo.")
    p = get_drink()
    print("Finally, let's order the side for your combo.")
    a = get_side()
    c = Combo("Combo", k, p, a, discount_for_combo)
    # print(str(c))
    # ask user for input and store it in combo object
    # a combo must include one burger, one side, and one drink
    return c


def order():
    possible_options = [1, 2, 3, 4]
    print("1 for a Burger.")
    print("2 for a Drink.")
    print("3 for a Side.")
    print("4 for a Combo.")
    choice = None
    while choice == None:
        f1 = input("Please enter your choice:")
        if int(f1) in possible_options:
            choice = int(f1)
    item = None
    if choice == 1:
        item = get_burger()
    elif choice == 2:
        item = get_drink()
    elif choice == 3:
        item = get_side()
    elif choice == 4:
        item = get_combo()
    return item


def take_order():
    # ask user for name for the order
    # repeat taking order until client is done
    # display order details
    # display a thank-you message

    print("Welcome to Ghana Burger Shop!")
    f1 = input("Please what is the name for the order? ")
    o = Order(f1)
    print("Can you say what you want")
    done = False
    while done == False:
        item = order()
        o.add_item(item)
        f1 = input("Do you need more items? (Enter n to stop.) ")
        if f1.lower() == "n":
            done = True
    return o


customer_order = take_order()
customer_order.display()

print("Thank you for choosing Ghana Burger Shop")
