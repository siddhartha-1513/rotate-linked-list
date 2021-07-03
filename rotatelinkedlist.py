class Node(object):

    def __init__ (self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next (self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n

    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d
        
    def to_string(self):
        return "Node Value:" + str(self.data)
        
    def has_next(self):
        if self.get_next():
            return True
        return False


class LinkedList (object):

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size (self):
        return self.size

    def add (self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1
    
    
    def rotatelinkedlist(self,k): # here we have to take care of "K" because it should be less then linkedList lenght .
        prev_node=None
        temp=self.root
        count=0
        while count !=k:
            prev_node=temp
            temp=temp.get_next()
            count+=1 
        
        prev_node.set_next(None)
        prev_node1=None
        current=temp
        while current:
            prev_node1=current
            current=current.get_next()
        
        prev_node1.set_next(self.root)
        self.root=temp
        return self.root
        
        
    def remove (self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True		# data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def find (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None
        
    def print_list(self):
        if self.root is None:
            return
        temp=self.root
        print(temp.to_string())
        while temp.has_next():
            temp=temp.get_next()
            print(temp.to_string())
            
        

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.add(4)
myList.add(7)
myList.print_list()
print("size="+str(myList.get_size()))
print("size="+str(myList.get_size()))
print("size="+str(myList.get_size()))
print(myList.find(5))
myList.print_list()
print("---------------list after rotate---------------")
myList.rotatelinkedlist(2)
myList.print_list()
