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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "income":0
}

def check_resources(o):
    if not MENU[o]["ingredients"]["water"] <= resources["water"]:
        return "water"
    elif not MENU[o]["ingredients"]["coffee"] <= resources["coffee"]:
        return "coffee"
    elif "milk" in MENU[o]['ingredients'] and not MENU[o]["ingredients"]["milk"] <= resources["milk"]:
        return "milk"
    else:
        return "enough"

machine_is_running = True
while machine_is_running:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}gr\nMoney: ${resources["income"]}")
        continue
    if order == "off":
        break
    if check_resources(order) != "enough":
        print(f"Sorry there is not enough {check_resources(order)}.")
        continue

    print("Please insert coins.")
    quarters = int(input("How many quarters?")) * 0.25
    dimes = int(input("How many dimes?")) * 0.1
    nickles = int(input("How many nickles?")) * 0.05
    pennies = int(input("How many pennies?")) * 0.01

    paid = quarters + dimes + nickles + pennies
    change = round(paid - MENU[order]["cost"], 2)

    if paid >= MENU[order]["cost"]:
        if change > 0:
            print(f"Here is ${change} in change.")
        resources['income'] += MENU[order]["cost"]
        resources['water'] -= MENU[order]["ingredients"]['water']
        resources['coffee'] -= MENU[order]["ingredients"]['coffee']
        if "milk" in MENU[order]["ingredients"]:
            resources['milk'] -= MENU[order]["ingredients"]['milk']
        print(f"Here is your {order} ☕ Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")



