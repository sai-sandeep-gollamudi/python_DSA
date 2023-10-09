#Binary Search Tree

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root= None

    def insert(self,value):
        new_node=Node(value)
        if(self.root==None):
            self.root=new_node
            return True
        temp=self.root
        while(True):
            if(temp.value==value):
                return False
            if(temp.value>value):
                if (temp.left is None):
                    temp.left = new_node
                    return True
                temp = temp.left

            else:
                if (temp.right is None):
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self,value):
        temp=self.root
        while(temp is not None):
            if(temp.value<value):
                temp=temp.right
            elif(temp.value>value):
                temp=temp.left
            else:
                return True
        return False

bst=BinarySearchTree()
bst.insert(45)
bst.insert(18)
bst.insert(22)
bst.insert(9)
bst.insert(7)

print(bst.contains(20))
print(bst.contains(7))

####################################

#Hash Table - seperate chaining

class HashTable:
    def __init__ (self,size=7):
        self.data_map = [None]*size

    def hash(self,key):
        hashmap=0
        for i in key:
            hashmap=(hashmap + ord(i)*23)%len(self.data_map)
        return hashmap

    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i," : ",val)

    def set_items(self,key,value):
        index=self.hash(key)
        if(self.data_map[index] is None):
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_items(self,key):
        index=self.hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if(self.data_map[index][i][0] == key):
                    return self.data_map[index][i][1]
        return None

    def key(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if(self.data_map[i] is not None):
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys




my_table= HashTable()

my_table.print_table()

my_table.set_items('just', 25)
my_table.set_items('checking', 30)
my_table.set_items('for', 35)
my_table.set_items('errors', 40)

print("Table values after using set_items: ")

my_table.print_table()

print(f"value for key 'checking' is : {my_table.get_items('checking')}")

print(f"All the key values are: {my_table.key()}" )

