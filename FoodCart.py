class dish:
    def __init__(self,dish_name,dish_price):
        self.dish_name = dish_name
        self.dish_price = dish_price

    def show_dish(self):
        print("------------------------------")
        print(self.dish_name," | ",self.dish_price)
        print("------------------------------")
    def amount(self,quantity):
            net_amount = quantity*self.dish_price
            return net_amount

class menu:
    def __init__(self,no_of_dishes,list_of_dishes):
        self.no_of_dishes = no_of_dishes
        self.list_of_dishes = list_of_dishes


    def show_menu(self):
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(self.no_of_dishes)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            for idx in range(len(self.list_of_dishes)):
                self.list_of_dishes[idx].show_dish()



def main():
    dish1 = dish("Dal Fry" , 180)
    dish2 = dish("Paneer Tikka Masala" , 240)
    dish3 = dish("Butter Naan",50)
    dish4 = dish("McAloo Tikki Burger",40)
    dish5 = dish("Coke",20)
    dishes = [dish1,dish2,dish3,dish4,dish5]
    dish_price = {
        dish1.dish_name:dish1.dish_price,
        dish2.dish_name: dish2.dish_price,
        dish3.dish_name: dish3.dish_price,
        dish4.dish_name: dish4.dish_price,
        dish5.dish_name: dish5.dish_price
    }
    menu1= menu(len(dishes),dishes)
    menu1.show_menu()

    item_names = []
    quantities = []
    food_cart = []

    while True:
        item_name = input("Enter Dish Name to add in Cart: ")
        quantity = int(input("Enter Dish Quantity: "))
        item_names.append(item_name)
        quantities.append(quantity)
        price = dish_price[item_name]*quantity
        food_cart.append(price)

        print(item_names)
        print(quantities)
        print(food_cart)

        choice = input("Do You wish to add more items? (yes/no)")
        if choice == "no":
            break

    amount = sum(food_cart)
    print("TOTAL AMOUNT: \u20b9", amount)
main()