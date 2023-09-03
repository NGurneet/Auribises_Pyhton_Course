
class Customer:

    def __init__(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age:" ))
        self.email = input("Enter Email: ")

    def show(self):
        print("Name:{name} Age:{age} Email:{email}".format_map(vars(self)))

def main():
    message = """Welcome to CRM App
        1: Add New Customer
        2: Delete Customer
        3: Update Customer
        4: View All Customers
        5: View Customer by Phone
        6: Exit
        """

    choice = int(input("Enter Your Choice: "))
    while(True):
        if choice ==1:
            customer1 = Customer()
            customer1.show()
        choice = int(input("Enter Your Choice: "))
        if choice ==6:
            break
if __name__=="__main__":
    main()

