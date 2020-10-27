
def possible_password(number=int):
    number = str(number)
    # It is a six-digit number.
    if len(number) != 6:
        return False
    #Going from left to right, the digits never decrease; 
    #they only ever increase or stay the same (like 111123 or 135679).
    else:
        if list(str(number)) != sorted(list(str(number))):
            return False
        else:
            for i in range(len(number) - 1):
                currentnumber = number[i]
                #Two adjacent digits are the same (like 22 in 122345).
                if number[i] == number[i + 1]:
                    return True
                else:
                    continue
    return False

'''
test_case1 = 111111
test_case2 = 223450
test_case3 = 123789
print (possible_password(test_case1))
print (possible_password(test_case2))
print (possible_password(test_case3))
'''

part1answer = 0
for i in range(138241,674034):
   if possible_password(i) == True:
       part1answer += 1
print (part1answer)

