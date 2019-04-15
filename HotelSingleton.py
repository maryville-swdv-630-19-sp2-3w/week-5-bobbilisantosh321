class Hotel:
    __instance = None
    
    def __init__(self):
        if Hotel.__instance != None:
            raise Exception("This class is a singleton")
        else:
            self.__name = "Novetel Hotel Pvt Ltd"
            self.__noofRooms = 200
            self.__bookedRooms = 0
            self.__noofEmployees = 0
            Hotel.__instance = self
    
    def setNoofEmployees(self, noofEmployees):
        self.__noofEmployees = noofEmployees
    
    def getNoofEmployees(self):
        return self.__noofEmployees
    
    def getNoofRooms(self):
        return self.__noofRooms
    
    def setBookedRooms(self, noofRooms):
        self.__bookedRooms = noofRooms
    
    def getBookedRooms(self):
        return self.__bookedRooms
    
    def getHotelName(self):
        return self.__name
    
    @staticmethod
    def getInstance():
        #static method for instance
        if Hotel.__instance == None:
            Hotel.__instance == Hotel()
        return Hotel.__instance


hotel1 = Hotel()
print("******** Creates singleton instance ******")
print("Hotel1 name is {0}".format(hotel1.getHotelName()))
hotel1.setNoofEmployees(150)
print("Hotel1 number of employees are {0}".format(hotel1.getNoofEmployees()))

print("****** Uses same created instance *******")
hotel2 = Hotel.getInstance()
print("Hotel number of employees are {0}".format(hotel2.getNoofEmployees()))
print("****** Changes the same singleton instance ********")
hotel2.setNoofEmployees(250)
print("Hotel number of employees are {0}".format(hotel1.getNoofEmployees()))
print("******* Restricts Instance Creation ********")
hotel3 = Hotel()


    
    
        