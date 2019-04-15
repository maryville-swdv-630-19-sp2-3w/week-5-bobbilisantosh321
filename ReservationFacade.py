#Facade Pattern for creating Reservation which includes creating a room and a customer
class Room:
    def __init__(self):
        self.__roomNo = None
        self.__isBooked = False
        self.__roomType = None
    
    def bookRoom(self, roomNo):
        self.__isBooked = True
        self.__roomNo = roomNo
    
    def getRoomNo(self):
        return self.__roomNo
    
    def isRoomBooked(self):
        return self.__isBooked
    
    def getRoomType(self):
        return self.__roomType
    
    def setRoomType(self, roomType):
        self.__roomType = roomType
        
    
class Customer:
    def __init__(self):
        self.__name = None
        self.__cusId = None
    
    def setCustomerDetails(self, cusId, name):
        self.__cusId = cusId
        self.__name = name
    
    def getCustomerId(self):
        return self.__cusId
    
    def getCustomerName(self):
        return self.__name

class Reservation:   
    def __init__(self):
        self.__customer = Customer()
        self.__room = Room()

    def reserveRoom(self, roomNo, roomType, cusName, cusId):
        self.__customer.setCustomerDetails(cusId, cusName)
        self.__room.setRoomType(roomType)
        self.__room.bookRoom(roomNo)
    
    def getCustomer(self):
        return self.__customer
    
    def getRoom(self):
        return self.__room

def main():
    reservation = Reservation()
    reservation.reserveRoom("506", "One Bed Room", "John", "34589")
    print("Reservation customer name is {0}".format(reservation.getCustomer().getCustomerName()))
    print("Reserved room is {0}".format(reservation.getRoom().getRoomNo()))

main()
    
    
    