# Coffee Machine Project.  Day 15 Project for 100 Days of Code: The Complete Python Pro Bootcamp
# for 2023 on Udemy by Dr. Angela Wu

from data import MENU, resources


# TODO: 3. Print report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Mile: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    if "money" in resources:
        print(f"Money: ${resources['money']:,.2f}")


# TODO: 4. Check resources sufficient?
def check_resources(drink):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']

    if 'water' in MENU[drink]['ingredients']:
        if water < MENU[drink]['ingredients']['water']:
            print("Sorry there is not enough water.")
            return False
    if 'milk' in MENU[drink]['ingredients']:
        if milk < MENU[drink]['ingredients']['milk']:
            print("Sorry there is not enough milk.")
            return False
    if 'coffee' in MENU[drink]['ingredients']:
        if coffee < MENU[drink]['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
            return False
    return True

# TODO: 5. Process Coins
def process_coins():
    total = 0
    quarters = int(input("How many Quarters?: "))
    total += quarters * 0.25
    dimes = int(input("How many Dimes?: "))
    total += dimes * 0.1
    nickles = int(input("How many Nickles?: "))
    total += nickles * 0.05
    pennies = int(input("How many Pennies?: "))
    total += pennies * 0.01
    return total

# TODO: 6. Check transaction successful?
def transaction(money, drink):
    amount_needed = MENU[drink]['cost']
    if money < amount_needed:
        print("Sorry that's not enough money.  Money refunded.")
        return False
    else:
        resources['money'] = money
        change = money - MENU[drink]['cost']
        print(f"Here if your ${change:,.2f} in change")
        return True

# TODO: 7. Make Coffee
def make_coffee(drink):
    if 'water' in MENU[drink]['ingredients']:
        water = MENU[drink]['ingredients']['water']
    else:
        water = 0
    if 'milk' in MENU[drink]['ingredients']:
        milk = MENU[drink]['ingredients']['milk']
    else:
        milk = 0
    if 'coffee' in MENU[drink]['ingredients']:
        coffee = MENU[drink]['ingredients']['coffee']
    else:
        coffee = 0

    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee

    print(f"Here is your {drink}.")


# TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
turn_off = False

while not turn_off:
    # TODO: 1.  Prompt user by asking "What would you like (espresso/latte/cappuccino):"
    choice = input("What would you like (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        turn_off = True

    if choice == "report":
        print_report()
    else:
        enough_resources = check_resources(choice)
        if not enough_resources:
            continue
        else:
            money_given = process_coins()
            make_drink = transaction(money_given, choice)
            if make_drink:
                make_coffee(choice)
            else:
                continue







