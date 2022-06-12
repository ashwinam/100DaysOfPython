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
money_earned = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

"""Mine Version Incomplete"""


def is_transaction_successful(coffee_payment, coffee_price):
    if coffee_payment < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
    elif coffee_payment > coffee_price:
        change = round(coffee_payment - coffee_price, 2)
        print(f"Here is ${change} dollars in change.")
    global money_earned
    money_earned += coffee_price


def check_resources(drink_option, resource):
    """If resources available it asks money else it prints not enough resources."""
    for each_item in drink_option:
        if drink_option[each_item] > resource[each_item]:
            print(f"Sorry there is not enough {each_item}.")
            return False
        return True


def process_coin():
    print("Please insert the coins.")
    total = int(input("How many quarters? $")) * 0.25
    total += int(input("How many dimes? $")) * 0.1
    total += int(input("How many nickles? $")) * 0.05
    total += int(input("How many pennies? $")) * 0.01
    return total


# let's start building the coffee machine.

is_machine_on = True

while is_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        print(f"Water  : {resources['water']}ml")
        print(f"Milk   : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Profit : ${money_earned}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"], resources):
            payment = process_coin()
            price_of_coffee = drink['cost']
            is_transaction_successful(payment, price_of_coffee)
            for item in drink["ingredients"]:
                resources[item] -= drink["ingredients"][item]
            print(f"Here is your {choice}☕. Enjoy!")
