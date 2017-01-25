operands = []
operators = []

def Node(data, next = None, prev = None):
    def get(msg = 'data'):
        nonlocal data, next, prev
        f = {'data': data, 'next': next, 'prev': prev}
        return f[msg]

    def set_new(msg, obj):
        nonlocal data, next, prev
        if msg == 'data':
            data = obj
        if msg == 'next':
            next = obj
        if msg == 'prev':
            prev = obj

    # def getitem(i):
    #     nonlocal data, next, prev
    #     if i == 0:
    #         return self
    #     return self.next[i-1]

    def toStr():
        nonlocal data, next, prev
        if prev: prev = prev['get']('data')
        else: prev = None
        if next: next = next['get']('data')
        else: next = None
        return '{0} <-- {1} --> {2}'.format(prev, data, next)

    def copy():
        nonlocal data, next, prev
        node = Node(data)
        if prev: node['get']('prev')['set'](prev['get']('data')) 
        if next: node['get']('next')['set'](next['get']('data'))
        return node

    dispatch = {'get' : get, 'set' : set_new, 'str' : toStr, 'copy' : copy} 
    return dispatch

def LinkedList(head = None, tail = None):
    def get(msg = 'head'):
        nonlocal head, tail
        f = {'head' : head, 'tail' : tail}
        return f[msg]

    def set_new(msg, obj):
        if msg == 'head':
            head = obj
        if msg == 'tail':
            tail = obj

    def addHead(data):
        nonlocal head, tail
        node = Node(data)
        if head == None:
            head = node
            tail = head
        else:
            node['set']('next', head) # node.next = self.head
            node['get']('next')['set']('prev', node) # node.next.prev = node
            head = node

    def addTail(data):
        nonlocal head, tail
        node = Node(data)
        if head == None:
            head = node
            tail = head
        else:
            node['set']('prev', tail) # node.prev = self.tail
            node['get']('prev')['set']('next', node) # node.prev.next = node
            tail = node

    def search(k):
        p = head
        if p != None:
            while p != None:
                if (p['get']('data') == k):
                    return p
                p = p['get']('next')
        return None

    def remove(p):
        nonlocal head, tail
        if p['get']('prev') != None: 
            p['get']('prev')['set']('next', p['get']('next'))
        else:
            head = (p['get']('next'))
        if p['get']('next') != None:
            p['get']('next')['set']('prev', p['get']('prev'))
        else: 
            tail = p['get']('prev')

    def toStr():
        s = '<'
        p = head
        if p != None:
            while p != None:
                s += str(p['get']('data'))
                p = p['get']('next')
        return s + '>'

    # def getitem(self, i):
    #     if i == 0:
    #         return self.head
    #     return self.head.next[i-1]

    def len():
        count = 0
        p = head
        if p != None:
            while p != None:
                p = p['get']('next')
                count += 1
            return count
        return 0

    def delHeadZero():
        p = head
        while p['get']('data') == 0:
            pNext = p['get']('next')
            if pNext:                
                remove(p)
                p = pNext
            else:                
                return        

    def copy():
        p = head
        l = LinkedList()
        while p:
            l['addTail'](p['get']())
            p = p['get']('next')
        return l

    dispatch = {'get' : get, 'set' : set_new,'str' : toStr, 'addHead' : addHead, 'addTail' : addTail, 'remove' : remove, 'search' : search, 'len' : len, 'delHeadZero' : delHeadZero, 'copy' : copy}
    return dispatch

def StrToLinkedList(str):
    l = LinkedList()
    for i in str:
        l['addTail'](int(i))
    return l

def Plus(list1, list2):
    def Add(x, y):
        return((int(x['get']('data')) if x is not None else 0) + (int(y['get']('data')) if y is not None else 0))
    l = LinkedList()
    l1, l2 = list1['copy'](), list2['copy']()
    p1, p2 = l1['get']('tail'), l2['get']('tail')
    while(p1 or p2):
        x = Add(p1, p2)
        l['addHead'](x % 10)
        if x // 10 > 0:
            if p1['get']('prev'):
                p1['get']('prev')['set']('data', int(p1['get']('prev')['get']('data')) + x // 10)
            else:
                p1['set']('prev', Node(x // 10)) # p1, list1 on head add's 1  
        if p1: p1 = p1['get']('prev')
        if p2: p2 = p2['get']('prev')
    return l

def Negative(l):
    l['delHeadZero']()
    Num = l['get']('head')['get']('data')
    Num = Num * (-1)
    l['get']('head')['set']('data',Num)
    return l

def IsBigger(list1, list2):
    LenL1 = list1['len']()
    LenL2 = list2['len']()
    if LenL1 == LenL2:
        Long, Short = list1['get']('head'), list2['get']('head')
        while Long:
            if Long['get']('data') > Short['get']('data'):
                return True
            elif Long['get']('data') < Short['get']('data'):
                return False
            Long = Long['get']('next')
            Short = Short['get']('next')
        else:
            None
    elif LenL1 > LenL2:
        return True
    elif LenL1 < LenL2:
        return False

def Sub(list1, list2):
    Flag = False
    Neg = False
    def Minus(x, y):
        nonlocal Flag
        X=int(x['get']('data')) if x is not None else 0
        Y=int(y['get']('data')) if y is not None else 0        
        if Flag == True:
            if Y==0:
                Y = 9
            else:
                Y=Y-1
                Flag = False

        if Y >= X:
            return Y-X
        else:
            Flag = True
            return (Y + 10) - X        
    l = LinkedList()
    if IsBigger(list1, list2) == True:
        Long, Short = list1['get']('tail'), list2['get']('tail')
        Neg = True
    elif IsBigger(list1, list2) == False:
        Short, Long = list1['get']('tail'), list2['get']('tail')
    else:
        l['addHead'](0)
        return l
    while(Long or Short):
        x = Minus(Short, Long)
        l['addHead'](x)
        if Long: Long = Long['get']('prev')
        if Short: Short = Short['get']('prev')
    if Neg:
        l = Negative(l)
    l['delHeadZero']()    
    return l

def Mul(list1, list2):
    def Mult(x, y):
        return((int(x['get']('data')) if x is not None else 0) * (int(y['get']('data')) if y is not None else 0))
    if type(list1) == int:
        OneL = LinkedList()
        OneL['addHead'](list1)
        return Mul(OneL,list2)
    tran = 0
    p1 = list1['get']('tail')
    sum = LinkedList()
    sum['addHead'](0)
    while p1:
        p2 = list2['get']('tail')
        rest = LinkedList()
        rest['addHead'](0)
        new_list = LinkedList()
        for i in range(tran):
            new_list['addTail'](0)
            rest['addTail'](0) 
        while p2:
            x = Mult(p1, p2)
            new_list['addHead'](x%10)
            rest['addHead'](x//10)
            p2 = p2['get']('prev')
        sum = Plus(new_list, sum)
        sum = Plus(rest, sum)
        p1 = p1['get']('prev')
        tran += 1
    return sum

def Div(list1, list2):
    def Division(list1, list2):
        b = IsBigger(list1, list2)
        k = 0
        if b:
            k = 1
            l = Plus(list2, list2)
            b = IsBigger(list1, l)
            while b:
                l = Plus(l, list2)
                k = k + 1
                b = IsBigger(list1, l)
        if b == None: # list1 == list2
            k = k + 1
        return k

    l = LinkedList()
    LenL1 = list1['len']()
    p1, p2 = list1['get']('head'), list2['get']('head')
    if(LenL1 == 1):
        d = p2['get']('data')
        while p2:
            div = d // p1['get']('data')
            l['addTail'](div)
            d = d - div * p1['get']('data')
            if p2['get']('next'):
                d = (d * 10) + p2['get']('next')['get']('data')
            p2 = p2['get']('next')
    else:
        d = LinkedList()
        d['addTail'](p2['get']('data'))
        while p2:
            div = Division(d, list1)
            l['addTail'](div)
            mul = Mul(div, list1)
            mul['delHeadZero']()
            d = Sub(mul, d)
            if p2['get']('next'):
                d['addTail'](p2['get']('next')['get']('data'))
            p2 = p2['get']('next')
    return l
    # print(l['str']())

def Pow(po, mu):
    l =  LinkedList()
    LOne = LinkedList()
    l['addHead'](2)
    LOne['addTail'](1)
    while po['get']('head')['get']('data') > 0:
        l = Mul(2, l)
        # l['delHeadZero']()
        po = Sub(LOne, po)
    l = Mul(l, mu)
    return l

def Apply(x):
    dispatch = {'+' : Plus, '-' : Sub, '*' : Mul, '/' : Div, '^' : Pow}
    return dispatch[x]

def Main():
    global operands, operators
    l = LinkedList()
    x = ''
    print("  ***Welcome to CalBomb***\nChoose one of the option :\n1)calculate. \n2)If you want to calculate press c\n3)If you want to print the numbers press p\n4) Exit Press q\n")
    while True:
        x = input('\nPlease enter a number : ')
        if x == 'q': return
        if (x in ('+', '-', '*', '/','^')):
            operators += x
        elif x=='c' or x=='C':
            Calc()
        elif x == 'p' or x =='P' :
            Print()
        else:
            Temp = True
            try:
                y = int(x)
            except ValueError:
                print("That's not an Number!")
                Temp = False
            if Temp == True:
                 l = StrToLinkedList(x)
                 operands += [l]

def Calc():
    global operands, operators
    while(len(operators) > 0):
        x = operators.pop()
        m = Apply(x)
        l = m(operands.pop(), operands.pop())
        l['delHeadZero']()
        operands += [l]

def Print():
    p = ''
    for i in operands:
        p += i['str']()
    print(p)

Main()

# l = LinkedList()
# l['addHead'](1)
# l['addHead'](2)
# l['addHead'](3)
# l['addHead'](4)
# ll = l['copy']()
# l['remove'](l['search'](1))
# l['delHeadZero']()
# print(l['str']())
# print(ll['str']())
