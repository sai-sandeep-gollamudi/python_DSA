#Single Linked List - remove duplicates
def binary_to_decimal(self):
    n = 0
    temp = self.head
    while (temp):
        n = n * 2 + temp.value
        temp = temp.next
    return n


