
print(f"Coffee Menu\nAmericano. Small: £3, Medium: £5, Large: £6")
class Coffee:
    def __init__(self,name,value):
        self.name = name
        self.value = value

    def check_budget(self,budget):

        if not isinstance(budget, (int,float)):
            print(input(f"Enter an integer or float please"))
            exit()
        if budget <= 2.99:
            print(f"Sorry insufficient funds!")
            exit()


    def get_change(self,budget):
        return budget - self.value

    def sell(self,budget):
        self.check_budget(budget)
        if budget >= self.value:
            purchase = input(f"You can buy a {self.name} coffee, would you like to contiue? ")
            if purchase == 'yes':
                print(f"Transaction complete, here is your change £{self.get_change(budget)}.")
            elif purchase == 'no':
                print(f"Okay goodbye")

            else:
                print(f"Here is your change {self.get_change(budget)}")
            exit('Goodbye')


small = Coffee('Small Americano', 2)
regular = Coffee('Regular Americano', 5)
big = Coffee('Big Americano', 6)

try:
    user_budget = float(input('What is your budget? '))
except ValueError:
    exit('Please enter a number')

for coffee in [big, regular, small]:
    coffee.sell(user_budget)
