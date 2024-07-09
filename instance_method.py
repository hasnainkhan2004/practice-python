class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet " 
        
ali = Payslips("ali", "no", 1000)
rayan = Payslips("rayan", "no", 2000)

print(ali.status(),"\n",rayan.status())

ali.pay()
print("After Payment")
print(ali.status(),"\n",rayan.status())