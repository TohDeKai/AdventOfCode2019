with open("AdventOfCode2019\Day03\Day03_PuzzleText.txt") as f:
	puzzle_list = f.read().splitlines()

wire_1 = puzzle_list[0]
wire_2 = puzzle_list[1]

test1_wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
test1_wire2 = "U62,R66,U55,R34,D71,R55,D58,R83"

x_axis = {"L":-1,"R":1,"U":0,"D":0}
y_axis = {"L":0,"R":0,"U":1,"D":-1}

def convert_to_xy_coordinates(wire):
    wire = wire.split(",")
    x = 0
    y = 0
    length = 0
    answer = {}
    for i in wire:
        direction = wire[0]
        magnitude = int(wire[1:])
        for i in range(magnitude):
            x += x_axis[direction]
            y += y_axis[direction]
            length += 1
            if (x,y) not in answer:
                 answer[(x,y)] = length
    return answer
print (convert_to_xy_coordinates(wire_1))