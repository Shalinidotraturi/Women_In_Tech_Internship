Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Node():
    
    def __init__(self, value, pred, next):
        self.value = value
        self.pred = pred
        self.next = next
        self.current = None
        
class LinkedList():
    """ Implements double linkend list. """
    
    def __init__(self):
        self.head = None
        self.tail = None 
        
   
    def __len__(self):
        p = self.head
        length = 0
        while p != None:
            p = p.next
            length += 1
        return length 
        
    def __iter__(self):
        self.current = self.head 
        return self
        
    def __next__(self): 
        if self.current is None:
            raise StopIteration
        else:
            ret = self.current.value 
            self.current = self.current.next
            return ret 
        
    def push(self, x):
        if self.tail is None:
            self.head  = Node(x, None, None)
            self.tail = self.head
        else:
            new_node = Node(x, self.tail, None)
            self.tail.next  = new_node
            self.tail = new_node 
            
    def pop(self):
        if self.tail is None:
            raise ValueError("empty list")
        
        val = self.tail.value 
        self.tail = self.tail.pred
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        
        return val 
        
    def shift(self):
        if self.head is None:
            raise ValueError("empty list")
        
        val = self.head.value
        self.head = self.head.next
        if self.head is not None:
            self.head.pred = None 
        else:
            self.tail = None
            
        return val 
        
    def unshift(self, x):
        if self.head is None:
            self.head = Node(x, None, None)
            self.tail = self.head
        else:
            new_node = Node(x, None, self.head)
            self.head.pred = new_node
            self.head = new_node
