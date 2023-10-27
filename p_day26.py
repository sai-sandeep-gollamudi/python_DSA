#Applying selection sort to sort linked list
def selection_sort(self):
    if (self.length < 2):
        return False
    temp = self.head
    for i in range(self.length):
        after = temp.next
        min = temp.value
        ind = temp
        while (after):
            if (min > after.value):
                min = after.value
                ind = after
            after = after.next
        if (min != temp.value):
            ind.value = temp.value
            temp.value = min
        temp = temp.next


#Insertion sort on linked list
    def insertion_sort(self):
        if(self.length<2):
            return
        for i in range(self.length):
            temp = self.head
            swap=0
            while(temp.next is not None):
                next_node = temp.next
                if(temp.value>next_node.value):
                    t=temp.value
                    temp.value=next_node.value
                    next_node.value=t
                    swap+=1
                temp=temp.next
            if(swap==0):
                return

#Bubble sort on linked list
    def bubble_sort(self):
        if (self.length < 2):
            return

        for i in range(self.length, 0, -1):
            count = i
            swap = 0
            temp = self.head
            while (count and temp.next is not None):
                next_node = temp.next
                if (temp.value > next_node.value):
                    t = temp.value
                    temp.value = next_node.value
                    next_node.value = t
                    swap += 1
                temp = temp.next
                count -= 1
            if swap == 0:
                return
