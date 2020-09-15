data = [1,2,3,4]

def sumNum(n):
    sum = 0
    for x in n:
        sum += x
    return 'sum ' + str(sum)


def removeData(n):
    if n:
        n.pop();
        return 'Data = ' + str(n)
    else:
        return 'No Data left'

def multNum(n):
    mult = 1
    for x in n:
      mult *= x

    return 'mult ' + str(mult)

def Choose(arg):
    choice = {
        1 : sumNum(data),
        2 : multNum(data),
        3 : removeData(data),
    }
    return choice.get(arg, "invalid option")

print('Enter what you want to do with the Data')
print(*data)
print('Enter 1 for Getting the Result of Summing the Data')
print('Enter 2 for Getting the Result of Multiplying the Data')
print('Enter 3 for Getting whatever Data is left')
x = input('')
print(Choose(int(x)))