data = [1,2,3,4]

def sumNum(n):
    sum = 0
    for x in n:
        sum += x
    return 'sum ' + str(sum)

def Choose(arg):
    choice = {
        1 : sumNum(data),
    }
    return choice.get(arg, "invalid option")

print('Enter what you want to do with the Data')
print(*data, sep= ' , ')
print('Enter 1 for Getting the Result of Summing the Data')
x = input('')
print(Choose(int(x)))