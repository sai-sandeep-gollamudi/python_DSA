
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1

    def print_stack(self):
        temp=self.top
        while(temp):
            print(temp.value)
            temp=temp.next

    def push(self,value):
        new_node=Node(value)
        if(self.height==0):
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1
        return True

    def pop(self):
        if(self.height==0):
            return None
        else:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            self.height-=1
            return temp

s=Stack(5)
s.push(6)
s.push(7)
print("Stack before poping: ")
s.print_stack()
s.pop()
print("Stack after poping: ")
s.print_stack()


#######################
#Queue

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1

    def print_queue(self):
        temp=self.first
        while(temp):
            print(temp.value)
            temp=temp.next

    def enqueue(self,value):
        new_node=Node(value)
        if(self.length==0):
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1

    def dequeue(self):
        if(self.length==0):
            return None
        elif(self.length==1):
            temp=self.first
            self.first=None
            self.last=None
        else:
            temp=self.first.next
            self.first.next=None
            self.first=temp
        self.length-=1
        return temp

q=Queue(10)
q.enqueue(11)
q.enqueue(12)
print("Queue before calling dequeue: ")
q.print_queue()
q.dequeue()
print("Queue after calling dequeue: ")
q.print_queue()



