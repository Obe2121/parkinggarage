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
        

    def take_ticket(self): #amount up or down by one
        pass    

    def pay_for_parking(self): #how are you going to pay 
        print("please pay")
    
    def leave_garage(self):#is your ticket paid or not
        while True:
            response = input('please input ticket number ')

garage_program = Parking_Garage()
ticket = (1,2,3,4,5,6,7,8,9,10)
parking_space = (1,2,3,4,5,6,7,8,9,10)
current_ticket = []
garage_program.run_program()
