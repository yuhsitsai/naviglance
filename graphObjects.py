class buildingObj() :
    """
        A custom class representing a building with a series of rooms represented by RoomObj objects and a given number of floors (where above ground floors come first, and then a basement would be n+1th floor).
    """

    # construct buildingObj with a name and number of floors
    def __init__(self, buildingName: str, numFloors: int):
        self.buildingName = buildingName
        self.roomList = []
        for room in range(numFloors):
            self.roomList.append([])

    # add a path between two rooms within the building; default 0 if not given length
    # so elevators can have length 10000 D':
    def addPath(self,  room1: 'roomObj', room2: 'roomObj', length = 0):
        if not length:
            length = straightDistance(room1, room2)
        room1.addNeighbor(room2, length)
        room2.addNeighbor(room1, length)

    # add a roomObj to a given building
    def addRoomObj(self, room: 'roomObj'):
        self.roomList[room.getFloor()-1].append(room)
    
    # retrieve a list of all rooms on a given floor
    def getFloor(self, floor: int):
        return self.roomList[floor-1]
    
    # retrieve a list of all rooms in the building
    def getRoomList(self):
        return self.roomList

    # get the number of floors in the building
    def getFloorNum(self):
        return len(self.roomList)

    # retrieve the room in building whose name matches the given string exactly
    def getRoomfromBuilding(self, RoomName):
        for floor in range(self.getFloorNum()):
            for node in self.roomList[floor]:
                if node.getRoomName() == RoomName:
                    return node

class roomObj () :
    """
        A custom class representing a room (or walking point) within a buildingObj building with a name, a designated floor, a dictionary of neighbors, and x and y coordinates.
    """

    # construct roomObj with a name, floor level, x position, and y position (relevant to its floormap)
    def __init__(self, roomName: str, floor: int, xPos: int, yPos: int):
        self.roomName = roomName
        self.floor = floor
        # neighborDict: keys are neighboring roomObjs, values are the distances between self and the nbr
        self.neighborDict: dict = {}
        self.xPos = xPos
        self.yPos = yPos

    # retrieve name of room
    def getRoomName(self):
        return self.roomName

    # retrieve floor of room
    def getFloor(self):
        return self.floor

    # buildingObj addPath method uses this to do bidirectional edges
    # honestly you really should never use this on its own instead of buildingObj's addPath
    def addNeighbor(self, neighbor: 'roomObj', length: int):
        self.neighborDict[neighbor] = length

    # return dictionary of neighbors; keys are neighbors to self, values are distances to said nbr
    def getNeighbors(self):
        return self.neighborDict
    
    # retrieve distanceToNeighbor; kind of a silly shortcut
    def distanceToNeighbor(self, neighbor: 'roomObj'):
        return self.neighborDict[neighbor]
    
    # return x position
    def getXPos(self):
        return self.xPos
    
    # return y position
    def getYPos(self):
        return self.yPos
    

# return the straight bird's eye distance between two rooms (presumably in the same building)
def straightDistance(room1: 'roomObj', room2: 'roomObj'):
        return ((room1.getXPos() - room2.getXPos())**2 + (room1.getYPos() - room2.getYPos())**2)**0.5