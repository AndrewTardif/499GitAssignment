data = [1,2,3,4]

def sumNum(n):
    sum = 0
    for x in n:
        sum += x
    return 'sum ' + str(sum)

<<<<<<< HEAD
def removeData(n):
    n.pop();
    return 'Data = ' + str(n)
=======
def multNum(n):
    mult = 1
    for x in n:
      mult *= x

    return 'mult ' + str(mult)
>>>>>>> refs/heads/MultiplyFunction

def Choose(arg):
    choice = {
        1 : sumNum(data),
<<<<<<< HEAD
        2 : removeData(n),
=======
        2 : multNum(data),
>>>>>>> refs/heads/MultiplyFunction
    }
    return choice.get(arg, "invalid option")

print('Enter what you want to do with the Data')
print(*data)
print('Enter 1 for Getting the Result of Summing the Data')
x = input('')
print(Choose(int(x)))