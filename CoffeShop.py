# CoffeeShop Project

customer_cup_size = {"small": 2, "medium": 3, "large": 4}
cup_size = input("Do you want small, medium, or large? ")
cost_of_cup = customer_cup_size[cup_size]

price_of_kind_coffee = {"brewed": 0, "espresso": 0.50, "cold brew": 1}
customer_kind_of_coffee = input("Do you want brewed, espresso, or cold brew ? ")
customer_choice_of_flavor = input("Do you want a flavored syrup ? (Yes or No) ")
cost_of_coffee = price_of_kind_coffee[customer_kind_of_coffee]

price_of_flavor_type = {"none": 0, "hazelnut": 0.50, "vanilla": 0.50, "caramel": 0.50}
customer_flavor_type = input("Do you want hazelnut, vanilla, or caramel ?")
if customer_choice_of_flavor == "yes" or customer_choice_of_flavor == "Yes":
    print(customer_flavor_type)
cost_of_flavor = price_of_flavor_type[customer_flavor_type]

coffee_total_price = cost_of_cup + cost_of_coffee + cost_of_flavor
tip = (coffee_total_price * 0.15) + coffee_total_price

print("You asked for a " + cup_size + " cup of " + customer_kind_of_coffee + " coffee with " + customer_flavor_type + " syrup ")
print("Your cup of coffee costs ", coffee_total_price)
print("The price with a tip is", tip)
