MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_enough(order_ingredients):
    """Returns True when order can be made, and False when ingredients are not enough."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


def process_coin():
    """Returns the total Calculated from the coins inserted."""
    print('Please insert coins.')
    total = int(input('how many quarters?')) * 0.25
    total += int(input('how many dimes?')) * 0.1
    total += int(input('how many nickles?')) * 0.05
    total += int(input('how many pennies?')) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost ):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def makeCoffee(drink_name, order_ingredients):
    """Deduct the required ingredients from thr resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


is_on = True


while is_on:
    choice = str(input("what would you like? (espresso/latte/cappuccino): "))
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_enough(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])



