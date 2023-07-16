class paytm_recharge:

    def __init__(self,conn_category="Prepaid/Postpaid",mobile_number = "+91 XXXXX-XXXXX",operator = "Airtel",circle = "Circle",amount = "Browse Plans"):
        self.conn_category = conn_category
        self.mobile_number = mobile_number
        self.operator = operator
        self.circle = circle
        self.amount = amount
#prepaid / postpaid
#Mobile Number
#operator
#Amount

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Connection Category: ",self.conn_category)
        print("Mobile Number: ",self.mobile_number)
        print("Operator: ",self.operator)
        print("Circle: ",self.circle)
        print("Amount: ",self.amount)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def main():
    recharge1 = paytm_recharge("Postpaid","98985 99221","Jio","Punjab","399")
    recharge2 = paytm_recharge("Prepaid","98985 99002","Airtel","Punjab","999")
    recharge3 = paytm_recharge()
    recharge1.show()
    recharge2.show()
    recharge3.show()

main()