class stack:
    def _init_(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
s=stack()
print(s.isEmpty())
s.push(1)
s.push('two')
s.peek()
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
print(s.pop())




class queue():
    def _init_(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        return self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q=queue()
print(q.isEmpty())
print(q.enqueue(8))
print(q.dequeue())
