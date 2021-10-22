# Python defines functions in order
# top to bottom
# Classes are created as a whole and don't adhere to this rule.

def getPosInt(prompt):
    while True:
        quantity = input(prompt)
        if quantity.isdigit():
            return int(quantity)
        else:
            print("Please enter a positive number.")

class ParkingGarage():
    def __init__(self, size):
        # print("Hello I have been created")
        self.spaces = [0 for i in range(size)] # 0 = empty space, otherwise it's the ticket number
        # The only property that varies between garages is the size of the garages.
        self.ticketsSold = 0 # Always zero for any new garage
        self.ticketStatus = {} # True = paid, False = unpaid

    def showGarageStatus(self):
        print(f"{self.ticketsSold} tickets have been sold.")
        print(f"There are {self.spaces.count(0)} available spaces")
        print(self.spaces)
        print(self.ticketStatus)


    def takeTicket(self):
        if 0 in self.spaces:
        # if self.spaces != []:
            self.ticketsSold = self.ticketsSold + 1
            self.spaces[self.spaces.index(0)] = self.ticketsSold
            # self.spaces = self.spaces - 1
            self.ticketStatus[self.ticketsSold] = False
            print(f'Your ticket number is {self.ticketsSold}')
        else:
            print('There are no spaces available in this parking garage.')
        

    #   pass
    # - This should increase the number of tickets sold by 1
    # - This should decrease the amount of parkingSpaces available by 1
    # - Add the ticket to the currentTicket dictionary with False(for unpaid)

    def payForParking(self,ticketnum = 0):
        # we decided it made more sense to make the payment a strict yes or no
        # hope that's ok
        # otherwise we would have made ticketStatus hold an amount left on the ticket to be paid
        # ask the user here how much they're paying towards it
        # subtract amount paid from ticketStatus up to the amount that's left to be paid for the ticket
        # if ticketStatus is 0, it means the ticket is paid for
        while True:
            if ticketnum == 0:
                ticketnum = getPosInt("Please enter your ticket number or enter '0' to exit.")
            if ticketnum == 0:
                return # quit out of function entirely

            if ticketnum in self.ticketStatus:
                if self.ticketStatus[ticketnum] == False:
                    while True:
                        userpayment = input("Your ticket number has not been paid yet. Pay ticket now ($5.00)? (y/n)").lower()
                        if userpayment == 'n':
                            print("Don't forget to pay.")
                            return
                        elif userpayment == 'y':
                            print('Your ticket has been paid. You have 15 minutes remaining.')
                            self.ticketStatus[ticketnum] = True
                            return
                        else:
                            ("Please enter 'y' or 'n'.")
                else:
                    print('This ticket number has already been paid for.')
                    break
            else:
                print('This is not a valid ticket number. Please enter a valid ticket number.')
                ticketnum = 0


    def leaveGarage(self):
        
        while True:

            ticketnum = getPosInt("Please enter your ticket number or enter '0' to exit.")
            if ticketnum == 0:
                return # quit out of function entirely
            # print(self.spaces)
            
            if ticketnum in self.spaces:
                # print(self.ticketStatus[ticketnum])
                if self.ticketStatus[ticketnum] == False:
                    while True:
                        userpayment = input("Leave parking garage and pay now? (y/n)").lower()
                        if userpayment == 'y':
                            self.payForParking(ticketnum)
                            # print(self.ticketStatus[ticketnum])
                            if self.ticketStatus[ticketnum]:
                                self.spaces[self.spaces.index(ticketnum)] = 0
                                print("Thank you for parking with us, have a nice day.")
                            else:
                                print("Don't forget to pay before you leave.")
                            return
                        elif userpayment == 'n':
                            print("Please do not forget to pay.")
                            return
                        else:
                            print("Please enter 'y' or 'n'.")
                else:
                    print("Thank you for parking with us, have a nice day.")
                    # self.spaces.replace[ticketnum, 0]
                    self.spaces[self.spaces.index(ticketnum)] = 0
                    return

        

def runGarage():
    while True:
        garageSize = getPosInt("How many spaces should the garage have?: ")
        if garageSize != 0:
            garage = ParkingGarage(garageSize)
            break
        else:
            print("A garage must have at least one space.")

    garagePrompt = \
"""
Choose an option:
1. Take new ticket
2. Pay for ticket
3. Leave garage
4. Show garage status
5. Quit program

"""
    while True:
        cmd = getPosInt(garagePrompt)
        print()
        if cmd == 1:
            garage.takeTicket()
        elif cmd == 2:
            garage.payForParking()
        elif cmd == 3:
            garage.leaveGarage()
        elif cmd == 4:
            garage.showGarageStatus()
        elif cmd == 5:
            return
        else:
            print("Please enter a valid option.")

runGarage()


#leaveGarage
# - If the ticket has not been paid, display an input prompt for payment
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - Update parkingSpaces list to increase availability by 1 

# You will need a few attributes as well:
# - tickets (sold) -> integer(counter of sorts)
# - parkingSpaces -> list
# - currentTicket (is ticket paid?) -> dictionary