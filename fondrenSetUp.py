from graphObjects import *

# trust issy this creates fondy
def setFondrenMap(FondrenLibrary):
    F101 = roomObj("Quad Entrance", 1, 454, 470)
    F102 = roomObj("Pavilion Entrance", 1, 456, 51)
    F103 = roomObj("Circulation Desk", 1, 545, 145) #W03
    F104 = roomObj("South Reading Room", 1, 280, 267)
    F105 = roomObj("Public PCs", 1, 563, 212) #N08
    F106 = roomObj("NetID PCs", 1, 590, 320) #E04
    F107 = roomObj("NetID PCs and Macs", 1, 350, 270) #S06
    F108 = roomObj("Woodson Research Center", 1, 417, 125)
    F109 = roomObj("New Items and Film Area", 1, 280, 429)

    R112 = roomObj("Study Room 112", 1, 326, 392)
    R113 = roomObj("Study Room 113", 1, 326, 415)
    R156 = roomObj("Study Room 156", 1, 718, 156)

    T101 = roomObj("Women's Restroom - 1st Floor", 1, 491, 247)
    T102 = roomObj("Men's Restroom - 1st Floor", 1, 491, 227)
    T103 = roomObj("Gender Neutral Restroom - 1st Floor", 1, 702, 186) #old n06

    EV_A1 = roomObj("Elevator A - 1st Floor", 1, 416, 426)
    EV_B1 = roomObj("Elevator B - 1st Floor", 1, 422, 249)
    EV_C1 = roomObj("Elevator C - 1st Floor", 1, 378, 182)
    EV_D1 = roomObj("Elevator D - 1st Floor", 1, 605, 182)

    ST_C1 = roomObj("Stairs C - 1st Floor", 1, 377, 182)
    ST_D1 = roomObj("Stairs D - 1st Floor", 1, 421, 228)
    ST_E1 = roomObj("Stairs E - 1st Floor", 1, 607, 224)
    ST_F1 = roomObj("Stairs F - 1st Floor", 1, 357, 355)
    ST_G1 = roomObj("Stairs G - 1st Floor", 1, 646, 383) #E09
    ST_J1 = roomObj("Stairs J - 1st Floor", 1, 487, 425)

    E101 = roomObj("E101", 1, 451, 409)
    E102 = roomObj("E102", 1, 380, 409)
    E103 = roomObj("E103", 1, 451, 331)
    E105 = roomObj("E105", 1, 590, 386)

    W101 = roomObj("W101", 1, 386, 178)
    W102 = roomObj("W102", 1, 458, 133)
    W104 = roomObj("W104", 1, 454, 237)

    N101 = roomObj("N101", 1, 625, 265)
    N102 = roomObj("N102", 1, 658, 338)
    N104 = roomObj("N104", 1, 708, 212)
    N105 = roomObj("N105", 1, 653, 228)
    N106 = roomObj("N106", 1, 675, 384)
    N107 = roomObj("N107", 1, 653, 160)
    N109 = roomObj("N109", 1, 510, 238)

    S101 = roomObj("S101", 1, 336, 218)
    S102 = roomObj("S102", 1, 411, 235)
    S103 = roomObj("S103", 1, 385, 343)
    S104 = roomObj("S104", 1, 310, 343)
    S105 = roomObj("S105", 1, 311, 405)

    # 2nd floor estimates
    F201 = roomObj("CPAC", 2, 295, 312)
    R201 = roomObj("Study Room 201", 2, 309, 239)
    R202 = roomObj("Study Room 202", 2, 400, 229)
    R203 = roomObj("Study Room 203", 2, 470, 247)
    R204 = roomObj("Study Room 204", 2, 495, 247)
    R205 = roomObj("Study Room 205", 2, 518, 247)
    R207 = roomObj("Study Room 207", 2, 400, 258)

    EV_B2 = roomObj("Elevator B - 2nd Floor", 2, 358, 262)
    ST_D2 = roomObj("Stairs D - 2nd Floor", 2, 358, 219)
    ST_E2 = roomObj("Stairs E - 2nd Floor", 2, 547, 229)
    ST_G2 = roomObj("Stairs G - 2nd Floor", 2, 595, 363)
    
    T201 = roomObj("Women's Restroom - 2nd Floor", 2, 435, 230)
    T202 = roomObj("Men's Restroom - 2nd Floor", 2, 435, 262)

    N201 = roomObj("N201", 2, 599, 224)
    N202 = roomObj("N202", 2, 581, 270)

    S201 = roomObj("S201", 2, 356, 241)
    S202 = roomObj("S202", 2, 400, 246)
    S203 = roomObj("S203", 2, 435,251)

    all_nodes = [
    F101, F102, F103, F104, F105, F106, F107, F108, F109,
    R112, R113, R156,
    T101, T102, T103,
    EV_A1, EV_B1, EV_C1, EV_D1,
    ST_C1, ST_D1, ST_E1, ST_F1, ST_G1, ST_J1,
    E101, E102, E103, E105,
    W101, W102, W104,
    N101, N102, N104, N105, N106, N107, N109,
    S101, S102, S103, S104, S105,
    F201, 
    R201, R202, R203, R204, R205, R207,
    EV_B2,
    ST_D2, ST_E2, ST_G2,
    T201, T202,
    N201, N202,
    S201, S202, S203
    ]

    for i in all_nodes:
        FondrenLibrary.addRoomObj(i)
        # add room to fondy

    pairs = [[F101, E101],
            [E101, ST_J1],
            [E101, EV_A1],
            [E101, E102],
            [E101, E103],
            [E102, EV_A1],
            [E102, S103],
            [S103, S104],
            [S103, ST_F1],
            [S103, F107],
            [S103, E103],
            [S104, S105],
            [S104, S101],
            [S104, F107],
            [F104, S104],
            [F104, S101],
            [S101, F104],
            [S105, R112],
            [S105, R113],
            [S105, F109],
            [F107, S102],
            [S101, S102],
            [S102, ST_D1],
            [S102, EV_B1],
            [S101, W101],
            [S102, W101],
            [W101, ST_C1],
            [W101, EV_C1],
            [W101, W102],
            [W102, F108],
            [W102, F102],
            [W102, F103],
            [W102, W104],
            [W104, S102],
            [W104, E103],
            [W104, N109],
            [N109, T101],
            [N109, T102],
            [F103, F105],
            [N109, F105],
            [F105, F106],
            [F106, N109],
            [F105, EV_D1],
            [F105, ST_E1],
            [F105, N101],
            [F103, N107],
            [N107, N105],
            [N105, N101],
            [N101, F106],
            [N101, N102],
            [N105, N102],
            [N105, N104],
            [N104, T103],
            [T103, R156],
            [R156, N107],
            [E103, F106],
            [F106, E105],
            [N102, N106],
            [N106, ST_G1],
            [E105, N106],
            [F106, N102],
            [ST_G2, N201],
            [ST_G2, N202],
            [N201, N202],
            [N202, ST_E2],
            [N202, R205],
            [R205, ST_E2],
            [R205, R204],
            [R204, R203],
            [R203, S203],
            [S203, T201],
            [S203, T202],
            [S203, S202],
            [S202, R202],
            [S202, R207],
            [S202, S201],
            [S201, ST_D2],
            [S201, EV_B2],
            [S201, R201],
            [R201, F201]
            ]

    for i in pairs:
        FondrenLibrary.addPath(i[0], i[1])

    cf_pairs = [[EV_B2, EV_B1], [ST_D2, ST_D1], [ST_E2, ST_E1], [ST_G2, ST_G1]]
    for i in cf_pairs:
        FondrenLibrary.addPath(i[0], i[1], 10000)

    return FondrenLibrary