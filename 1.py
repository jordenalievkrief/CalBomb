stack = []

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __getitem__(self, i):
        if i == 0:
            return self
        return self.next[i-1]

    def __str__(self):
        if self.prev: prev = self.prev.data
        else: prev = None
        if self.next: next = self.next.data
        else: next = None
        return '{0} <-- {1} --> {2}'.format(prev,self.data,next)

class LinkedList:
    def __init__( self ):
        self.head = None
        self.tail = None

    def addHead(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def addTail(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            node.prev.next = node
            self.tail = node

    def search(self, k):
        p = self.head
        if p != None:
            while p != None:
                if (p.data == k):
                    return p
                p = p.next
        return None

    def remove(self, p):
        if p.prev != None: p.prev.next = p.next
        else: self.head = p.next
        if p.next != None: p.next.prev = p.prev
        else: self.tail = p.prev

    def __str__(self):
        s = '<'
        p = self.head
        if p != None:
            while p != None:
                s += str(p.data)
                p = p.next
        return s + '>'

    def __repr__(self):
        return str(self)

    def __getitem__(self, i):
        if i == 0:
            return self.head
        return self.head.next[i-1]

    def __len__(self):
        count = 0
        p = self.head
        if p != None:
            while p != None:
                p = p.next
                count += 1
            return count
        return 0

def StrToLinkedList(str):
    l = LinkedList()
    for i in str:
        l.addTail(i)
    return l

def Plus(list1, list2):
    def Add(x, y):
        return((int(x.data) if x is not None else 0) + (int(y.data) if y is not None else 0))
    l = LinkedList()
    p1, p2 = list1.tail, list2.tail
    while(p1 or p2):
        x = Add(p1, p2)
        l.addHead(x % 10)
        if x // 10 > 0:
            if p1.prev:
                p1.prev.data = int(p1.prev.data) + x // 10
            else:
                p1.prev = Node(x // 10)
        if p1: p1 = p1.prev
        if p2: p2 = p2.prev
    return l

def Insert():
    global stack
    l = LinkedList()
    l.addHead(None)
    while(l.head.data != 'q'):
        l = StrToLinkedList(input('Put the number:   '))
        if(l[0].data == '+'):
            l = Plus(stack.pop(), stack.pop())
        print(l)
        stack += [l]
    stack.pop()

Insert()
print(stack)
