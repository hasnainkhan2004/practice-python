class Employees:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password) ->None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + "days"
    
ali = Supervisors("Ali" , "A","xyz")

bilal = Chefs("Bilal" , "B")
rayan = Chefs("Rayan" , "R")

print(bilal.leave_request(3))
print(ali.password)
print(bilal.name)