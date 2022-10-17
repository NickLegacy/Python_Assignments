
class parking_garage():

    def __init__(self):
        self.tickets = []
        self.parking_spaces = []
        self.current_ticket = {}

    def take_ticket(self):

        if len(self.parking_spaces) == 0:
            print("Parking garage is full")

        else:
            self.tickets.remove(self.tickets[-1])
            self.parking_spaces.remove(self.parking_spaces[-1])

    def pay_for_parking(self):

        amount = input("Press y to pay ticket.")

        if amount == "y":

            self.current_ticket["Paid"] = True
            print("ticket has been paid, you have 15 minutes to leave.")

    def leave_garage(self):

        if self.current_ticket["Paid"] == True:
            print("Thank you, have a nice day!")

        else:

            amount = input("Press y to pay.")

            while amount != "y":
                amount = input("Press y to pay.")

            self.tickets.append(self.tickets[-1]+1)
            self.parking_spaces.append(self.parking_spaces[-1]+1)

def main():
    
    car = parking_garage()
    print("This is the parking garage.")
    print("Please take ticket.")

    take_ticket = input("Press y to take ticket.")

    if take_ticket.lower() == "y":
        
        car.take_ticket()
        car.pay_for_parking()
        car.leave_garage()

    else:
        print("Please take ticket")

main()
