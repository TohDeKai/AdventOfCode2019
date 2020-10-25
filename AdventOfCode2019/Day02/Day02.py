with open("AdventOfCode2019\Day02\Day02_PuzzleText.txt") as f:
    puzzle_list = [int(x) for x in f.readline().split(',')]
from itertools import product
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

def Intcode(my_list,noun,verb):
    # Made a copy of the list so original data will not be replaced
    copiedlist = my_list.copy()
    opcode = 0
    copiedlist[1] = noun
    copiedlist[2] = verb
    while copiedlist[opcode] != 99:
        if copiedlist[opcode] == 1:
            #addition
            result = copiedlist[copiedlist[opcode+1]] + copiedlist[copiedlist[opcode+2]]        
        elif copiedlist[opcode] == 2:
            #multiplication
            result = copiedlist[copiedlist[opcode+1]] * copiedlist[copiedlist[opcode+2]]
        copiedlist[copiedlist[opcode+3]] = result
        opcode += 4
    return copiedlist[0]

'''
print (Intcode(test1)==test1output)
print (Intcode(test2)==test2output)
print (Intcode(test3)==test3output)
print (Intcode(test4)==test4output)
print (Intcode(test5)==test5output)
'''

#For Part 1:
print (Intcode(puzzle_list,12,2))

#For Part 2:
address_range = range(0,100)
for x,y in product(address_range,address_range):
    if Intcode(puzzle_list,x,y) == 19690720:
        ans_noun = x
        ans_verb = y
print (100*ans_noun + ans_verb)