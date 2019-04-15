#Factory pattern for creating rooms

class Room(object):
    def __init__(self, booked):
        self.__booked = False
    
    def bookRoom(self):
        self.__booked = True
    
    def isRoomBooked(self):
        return self.__booked


class OneBedRoom(Room):
    def __init__(self):
        self.__type = "One Bed Room"
        self.__maxAccom = 2
    
    def getRoomType(self):
        return self.__type
    
    def getMaxAccom(self):
        return self.__maxAccom
    
class TwoBedRoom(Room):
    def __init__(self):
        self.__type = "Two Bed Room"
        self.__maxAccom = 4
    
    def getRoomType(self):
        return self.__type
    
    def getMaxAccom(self):
        return self.__maxAccom

class RoomFactory():
    def create_room(self, typ):
        return globals()[typ]()

room_obj = RoomFactory()
rooms = ["OneBedRoom", "TwoBedRoom"]
for eachRoom in rooms:
    print("Room Type is {0}".format(room_obj.create_room(eachRoom).getRoomType()))
    print("Room Maximum Accomodation is {0}".format(room_obj.create_room(eachRoom).getMaxAccom()))
    print("*************************************************************")
    
    