from collections import OrderedDict
class LRUCache:
      
    def __init__(self, cap):
        #code here
        self.capacity = cap 
        self.d = OrderedDict()
        

    def get(self, key):
        #code here
        if key in self.d:
            self.d.move_to_end(key)
            return self.d[key]
        return -1
        

    def put(self, key, value):
        #code here
        if key in self.d:
            self.d.move_to_end(key)
        self.d[key] = value 
        if len(self.d) > self.capacity:
            self.d.popitem(last=False)
        