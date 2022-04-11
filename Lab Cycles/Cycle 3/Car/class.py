'''
Design a class to store the details of a vehicle such as engine number, 
model, type, mileage, vendor, registration number, and owner name.
Design another class that holds the details of several vehicles and
provide functions to 
• Display the details of the collection
• Sort the collection according to mileage 
• Add, Delete and Modify the entries from the collection
• Store and Load the collection as a pickle file
• Filter the result according to the attributes and export it as a
report.
https://pbpython.com/pdf-reports.html
'''


class car:
    def __init__(self,C_EngNo,C_Model,C_Type,C_Vendor,C_RegNo,C_OwnName):
        self.C_EngNo = C_EngNo
        self.C_Model = C_Model
        self.C_Type = C_Type
        self.C_Vendor = C_Vendor
        self.C_RegNo = C_RegNo
        self.C_OwnName = C_OwnName
    

class CarDetails:
    Cars = list()
    def __init__():
        #Load from the pickle file
        pass
    def add_Car(Car):
        list.append(Car)
    def show_details():
        pass
        #Prints the car details
    def Sort_Mileage():
        #lambda for sorting
        pass
    def Delete_car():
        pass
    def Modify_car():
        pass
    def Save_Details():
        #Save as a pickle file
        pass
    def Create_report():
        #Create a report using pandas
        #Using lambda to sort the functions
        pass