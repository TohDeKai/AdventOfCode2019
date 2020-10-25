puzzle_text = open("AdventOfCode2019\Day02\Day02_PuzzleText.txt",'r')
file = puzzle_text.read()
puzzle_list = []
for i in file:
    if i != ',':
        puzzle_list.append(i)
puzzle_text.close()
#print (puzzle_list[:10])

'''
test1 = [1,9,10,3,
2,3,11,0,
99,
30,40,50]
test1output = [3500,9,10,70,
2,3,11,0,
99,
30,40,50]
test2 = [1,0,0,0,99]
test2output = [2,0,0,0,99]
test3 = [2,3,0,3,99]
test3output = [2,3,0,6,99]
test4 = [2,4,4,5,99,0]
test4output = [2,4,4,5,99,9801 ]
test5 = [1,1,1,4,99,5,6,0,99]
test5output = [30,1,1,4,2,5,6,0,99]
'''

def Intcode(my_list):
    # Made a copy of the list so original data will not be replaced
    copiedlist = my_list.copy()
    opcode = 0
    while copiedlist[opcode] == 1 or copiedlist[opcode] == 2 or copiedlist[opcode] == 99:
        if copiedlist[opcode] == 1:
            #addition
            result = copiedlist[copiedlist[opcode+1]] + copiedlist[copiedlist[opcode+2]]
            copiedlist[copiedlist[opcode+3]] = result
            opcode += 4
        elif copiedlist[opcode] == 2:
            #multiplication
            result = copiedlist[copiedlist[opcode+1]] * copiedlist[copiedlist[opcode+2]]
            copiedlist[copiedlist[opcode+3]] = result
            opcode += 4
        elif copiedlist[opcode] == 99:
            #halt
            break
    return copiedlist

'''
print (Intcode(test1)==test1output)
print (Intcode(test2)==test2output)
print (Intcode(test3)==test3output)
print (Intcode(test4)==test4output)
print (Intcode(test5)==test5output)
'''
#before running program, replace position 1 with the value 12 and replace position 2 with the value 2

puzzle_list[1] = 12
puzzle_list[2] = 2

print (Intcode(puzzle_list)[0])


