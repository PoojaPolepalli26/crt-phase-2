class queue:
    def __init__ (self):
        self.values=[]
    def enqueue(self,x):
        self.values.append(x)
    def dequeue(self):
        self.values.pop(0)
    def printvalues(self):
        print(self.values)
s=queue()
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
s.enqueue(40)
s.printvalues()
s.dequeue()
s.dequeue()
s.printvalues()










'''def enqueue(q,ele):
    q.append(ele)
    print(ele,"inserted successfully")
def dequeue(q):
    if len(q)==0:
        print("empty queue")
    print(q[0],"deleted successfully")
    q.pop()
queue=[]
enqueue(queue,10)
enqueue(queue,20)
enqueue(queue,30)
enqueue(queue,40)

dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)'''

