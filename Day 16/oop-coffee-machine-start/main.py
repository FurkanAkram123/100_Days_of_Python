from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



def main():
    
    machine_on = True
    while machine_on:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ")
        if choice == "off":
            machine_on = False
        elif choice == "report":
            coffee_machine.report()
            money_machine.report()
        else:
            #Check if the drink exists in the menu?
            drink = menu.find_drink(choice)

            #check if resources are sufficient to make the drink and if the payment is successful
            if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
    
if __name__ == "__main__":
    menu = Menu()
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()

    main()