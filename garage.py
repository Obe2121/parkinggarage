from IPython.display import clear_output

class Parking_Garage():
    def __init__(self):
        pass
    
    def run_program(self):
        clear_output
        while True:
            response = input("What would you like to do? Park, Pay, or Leave ")
            if response.lower() == "park":
                self.take_ticket()
            
            elif response.lower() == "pay":
                self.pay_for_parking()
                
            elif response.lower() == "leave":
                self.leave_garage()

            elif response.lower == "quit":
                  break
        

    def take_ticket(self): #amount up or down by one
            ticket_num = ticket
            space_num = parking_space.pop(0)
            current_tickets[ticket.pop(0)] = "unpaid"
            print(ticket)
            print(current_tickets)

  
    def pay_for_parking(self): #how are you going to pay 
        while True:
            response = input('Please input Ticket Number ')
            if response == current_tickets[key]:
                input("Press any key to pay")
                current_ticket[ticket] = "paid"
          
            else:
                print("Please input a valid Ticket Number")

    
    def leave_garage(self):#is your ticket paid or not
        while True:
            key = input('please input ticket number ')
            if key == key in current_tickets and value == "paid":
                current_ticket.pop(key)
                ticket.append(key)
                parking_space.append(key)
                print("Have a good Day!")

            else:
                print("Please Pay your Ticket")
            
            
              
garage_program = Parking_Garage()
current_tickets = {} 
ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parking_space = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
garage_program.run_program()
                 
                  
                  