stack = []

def Plus(listMax, listMin):
    if len(listMax) < len(listMin):
        listMax, listMin = listMin, listMax
    for i in range(len(listMax) - len(listMin)):
        listMin.insert(0, None)
    def Add(x, y):
        return((int(x) if x is not None else 0) + (int(y) if y is not None else 0))
    listZip = tuple(zip(listMax, listMin))
    a = 0
    for i in reversed(range(len(listZip))):
        listMax[i] = a // 10
        a = Add(*listZip[i])
        listMax[i] += a
        listMax[i] = listMax[i] % 10
    a = a // 10
    if a > 0:
        listMax.insert(0, a) 
    return listMax

def Insert():
    global stack
    list = [None]
    while(list[0] != 'q'):
        list = []
        list += input()
        if(list == ['+']):
            list = Plus(stack.pop(), stack.pop())
        print(list)
        stack += [list]
    stack.pop()

Insert()
print(stack)