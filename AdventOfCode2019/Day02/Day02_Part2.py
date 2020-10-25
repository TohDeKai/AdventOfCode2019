with open("AdventOfCode2019\Day02\Day02_PuzzleText.txt") as f:
    puzzle_list = [int(x) for x in f.readline().split(',')]

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
            copiedlist[copiedlist[opcode+3]] = result
            opcode += 4
        elif copiedlist[opcode] == 2:
            #multiplication
            result = copiedlist[copiedlist[opcode+1]] * copiedlist[copiedlist[opcode+2]]
            copiedlist[copiedlist[opcode+3]] = result
            opcode += 4
    return copiedlist[0]

for x in range(100):
    for y in range(100):
        if Intcode(puzzle_list,x,y) == 19690720:
            ans_noun = x
            ans_verb = y
print (100*ans_noun + ans_verb)