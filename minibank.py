from rich.console import Console
from rich.prompt import Prompt

def ptint_menu(consele):
    consele.print(
        "----------------Menu---------------"
        "1- yangi bank hisob raqimini ochish   "
        "2- pul qoyish (desposit) "
        "3- pul yechib olish (withdraw) "
        "4- hisobdagi balansni korish "
        "5- akaunt chiqish "
       "6- dasturdan chiqish "
        "------------------------------------",
        style = "red"
                                )
    
def print_new_line():
    print()

def create_akaunt(console):
    console.print("akaunt creation", style = "blue")
    name = input("enter your name: ")

    return name

def desposit(balanse):
    amount = float(input("amaount: "))
    if amount > 0 and amount <= balance:
        balance -= amount

        return balance
    
def check_balance(console, balance):
    console.print(f"your balanse: {balanse}", style ="green")

def check_user(user):
    return user is not None

def main():
    console = Console()
    user = None
    balance = None

    while True:
        print_menu(console)

        choice = Prompt.ask("Select menu: ", choices=["1", "2", "3", "4", "5", "6"],default="6")
        print_new_line()

        if chois == "1":
            user = create_akaunt(console)
            balanse = 0 
            console.print("Account has been created successfully", style="green")
            print_new_line()
        elif choice == "2":
            if check_user(user):
                balance = deposit(balance)
            else:
                console.print("no account, you have to create.",style="red")
        elif chois == "3":
            if check_user(user):
                balance = withdraw(balance)
            else:
                console.print("no akaunt,you have to create.",style="green")
        elif choise == "4":
            if check_user(user):
                check_balance(console,balance)
            else:
                console.print("no akaunt,you have to create.",style="green")
        elif choise == "5":
            user = None
            balance = None
            print("you has been logged out")
        elif choise == "6":
            break
 
main()