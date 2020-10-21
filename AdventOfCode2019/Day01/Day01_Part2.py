puzzle_text = open("AdventOfCode2019\Day01\Day01_PuzzleText.txt",'r')
file = puzzle_text.read()
puzzle_list = file.split()
puzzle_text.close()

def find_fuel(module):
    fuel = module
    total_fuel = 0
    while True:
        fuel = fuel //3 -2
        if fuel > 0:
            total_fuel += fuel
        else:
            break
    return total_fuel
    
    
total_fuel_all_modules = 0
for i in puzzle_list:
    total_fuel_all_modules  += find_fuel(int(i))
    
print (total_fuel_all_modules )