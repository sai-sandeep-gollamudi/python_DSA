
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def print_list(self):
        for value in self.adj_list:
            print(value, ':', self.adj_list[value])

    def add_edge(self,v1,v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self,v1,v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self,v):
        if v in self.adj_list:
            for ov in self.adj_list[v]:
                self.adj_list[ov].remove(v)
            del self.adj_list[v]
            return True
        return False


g=Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','C')
g.add_edge('A','D')
g.add_edge('B','D')
g.add_edge('C','D')
g.remove_vertex('D')
g.print_list()

#max heap
class MaxHeap:
    def __init__(self):
        self.heap = []

    def left_child(self,index):
        return 2*index + 1

    def right_child(self, index):
        return 2*index + 2

    def parent(self, index):
        return (index -1)//2

    def swap(self,index1,index2):
        self.heap[index1],self.heap[index2] = self.heap[index2],self.heap[index1]

    def insert(self,value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while(current>0 and self.heap[current] > self.heap[self.parent(current)]):
            self.swap(current,self.parent(current))
            current=self.parent(current)

    def remove(self):
        if(len(self.heap) == 0):
            return None

        if(len(self.heap) == 1):
            return self.heap.pop()

        mv = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink_down(0)
        return mv

    def sink_down(self,index):
        max = index
        l=len(self.heap)
        if(l == 0 or l == 1):
            return

        while True:
            left = self.left_child(index)
            right = self.right_child(index)

            if(left < l and self.heap[left] > self.heap[max] ):
                max = left

            if(right < l and self.heap[right] > self.heap[max]):
                max = right

            if(max != index):
                self.swap(index,max)
                index=max
            else:
                return




h = MaxHeap()
h.insert(99)
h.insert(72)
h.insert(61)
h.insert(58)

print(h.heap)

h.insert(100)
print(h.heap)

h.remove()
print(h.heap)

h.insert(120)
h.insert(110)
h.insert(85)
h.remove()
print(h.heap)
