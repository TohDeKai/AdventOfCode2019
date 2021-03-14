
puzzle_text = open("AdventOfCode2020\puzzletextday01.txt",'r')
file = puzzle_text.read()
puzzle_list = file.split()
puzzle_text.close()
X = puzzle_list

n = len(X)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if int(X[i]) + int(X[j]) + int(X[k])== 2020:
                print ('euraka!',int(X[i])*int(X[j])*int(X[k]))