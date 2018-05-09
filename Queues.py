#Queues are first in first out
#Stacks are first in last out

class Queue():
    #Initialize
    def __init__(self):
        self.items = []

    #Enqueue
    def enqueue(self, item):
        #Insert index and item
        #First item gets pushed to back
        return self.items.insert(0,item)

    #Deqeue
    def dequeue(self):
        return self.items.pop()

    #Show the array
    def list(self):
        for x in self.items:
            print(x)

#q is an instance of the class and is a type of Queue
q=Queue()
q.enqueue('moo')
q.enqueue('oink')
print("poped")
print(q.dequeue())
q.list()
