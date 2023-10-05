class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
        return True

    def print_list(self):
        temp=self.head
        while(temp is not None):
            print(temp.value)
            temp=temp.next

    def pop(self):
        if(self.length==0):
            return None
        elif(self.length==1):
            self.head=None
            self.tail=None
            self.length=0
        else:
            temp=self.tail
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
            self.length-=1
        return True

    def prepend(self,value):
        new_node=Node(value)
        if(self.length==0):
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.pre=new_node
            self.head=new_node
        self.length+=1
        return True

    def pop_first(self):
        if(self.length==0):
            return None
        elif(self.length==1):
            temp=self.head
            self.head=None
            self.tail=None
        else:
            temp=self.head
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
        self.length-=1
        return temp
