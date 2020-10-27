with open("AdventOfCode2019\Day03\Day03_PuzzleText.txt") as f:
	puzzle_list = f.read().splitlines()

wire_1 = puzzle_list[0]
wire_2 = puzzle_list[1]
wire_1 = wire_1.split(",")
wire_2 = wire_2.split(",")

test1_wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
test1_wire2 = "U62,R66,U55,R34,D71,R55,D58,R83"

import itertools

def convert_to_x_y_coordinates(wire):
    directions = wire.split(",")
    x = 0
    y = 0
    x_coordinates = []
    y_coordinates = []
    coordinates = []
    for direction in directions:
        if direction[0] == 'U':
            y += int(direction [1:])
        elif direction[0] == 'D':
            y -= int(direction [1:])
        elif direction[0] == 'L':
            x -= int(direction [1:])
        elif direction[0] == 'R':
            x += int(direction [1:])
        x_coordinates.append(str(x))
        y_coordinates.append(str(y))

    # return coordinates
    # Converting coordinates within list from strings to lists
    # coordinates = [[coordinate] for coordinate in coordinates] 
    
    
#Each element in coordinates is where wire changes direction
# print (convert_to_x_y_coordinates(test1_wire1))