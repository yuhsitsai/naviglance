from graphObjects import *
from pathFinder import *
from matplotlib import image
from matplotlib import pyplot as plt

def executeFindPath(building : buildingObj, room1 : roomObj, room2 : roomObj) :
    """
        Given a building and two rooms within it (that are not the same), finds the efficient path between them. Plots a graph with the route for each floorplan and saves a png of that superimposed route.
    """
    # calculates exact path
    exactPath = findPathMap(building, room1, room2)

    # gets floorplan for end floor
    mapImage = image.imread('fondren_floor_'+str(room2.getFloor())+'.png')

    ## test code, let it live
    # readablePath = {}
    # for key, value in exactPath.items():
    #     readablePath[key.getRoomName()] = value.getRoomName()
    # print(readablePath)
    
    # calls the function to plot the routes segmented by floor on correct floor plan
    floorChange = abs(room1.getFloor() - room2.getFloor())
    currEnd = room2
    floorsChanged = 0
    while floorsChanged < floorChange:
        for key, value in exactPath.items():
            if key.getFloor() != value.getFloor():
                plotRoute(exactPath, mapImage, key, currEnd)
                mapImage = image.imread('fondren_floor_'+str(value.getFloor())+'.png')
                currEnd = value
                break
        floorsChanged += 1
    plotRoute(exactPath, mapImage, room1, currEnd)

    # no return atm

def plotRoute(pathList, mapImage, startNode, endNode) :
    """
        Superimposes the path between the given start and end nodes on the provided mapImage floorplan.
        Shows the route map and saves it. 
    """

    # set up figure & background
    fig, ax = plt.subplots()
    plt.imshow(mapImage)

    # plot start and end points
    plt.plot(startNode.getXPos(), startNode.getYPos(), marker = '*', markersize = 8, color = "deeppink")
    plt.plot(endNode.getXPos(), endNode.getYPos(), marker = '*', markersize = 8, color = "deeppink")


    # plot path purely between start and end (doesn't use entirety of pathList)
    currNode = endNode
    while currNode is not startNode:
        plt.plot([currNode.getXPos(), pathList[currNode].getXPos()],
                 [currNode.getYPos(), pathList[currNode].getYPos()], 
                 lw=2, 
                 color="deeppink")
        currNode = pathList[currNode]

    # remove box and axes around plot
    plt.box(False)
    plt.xticks([])
    plt.yticks([])

    # show
    plt.show()

    # saves to png
    print('path'+str(startNode.getFloor())+'.png')
    plt.savefig('path'+str(startNode.getFloor())+'.png')