puzzle_text = open("AdventOfCode2019\Day01\Day01_PuzzleText.txt",'r')
file = puzzle_text.read()
puzzle_list = file.split()
puzzle_text.close()

def find_fuel(module):
    fuel = module // 3 - 2
    return fuel

total_fuel = 0

for i in puzzle_list:
    total_fuel += find_fuel(int(i))
    
print (total_fuel)