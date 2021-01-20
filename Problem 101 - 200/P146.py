import collections
'''
The key point in this problem is to efficiently remove
an item from / add an item on one end / pop an item from
the other end, from a container.
Double linked list has this property: constant time remove
a node and add or pop a node from either end.
'''
# native class implementation
class LRUCache_naive:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = dict()
        self.LRU_queue = collections.deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.LRU_queue.remove(key)
            self.LRU_queue.append(key)
            return self.cache[key]
        else:
            return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.LRU_queue.remove(key)
        elif len(self.cache) == self.size:
            LRU_key = self.LRU_queue.popleft()
            del self.cache[LRU_key]
        self.LRU_queue.append(key)
        self.cache[key] = value

# double linked list with hashtable(python dictionary)
class DL_list:
    def __init__(self, key: int, value: int, pre=None, post=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.post = post

class LRUCache_double_list:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = dict()
        # double linked list maintained by a head and a tail.
        self.head = DL_list(0, 0)
        self.tail = DL_list(0, 0)
        self.head.post = self.tail
        self.tail.pre = self.head

    def DL_remove(self, node: DL_list) -> None:
        pre_node = node.pre
        post_node = node.post
        pre_node.post = post_node
        post_node.pre = pre_node

    # add at the tail
    def DL_append(self, node: DL_list) -> None:
        last_node = self.tail.pre
        last_node.post = node
        self.tail.pre = node
        node.pre = last_node
        node.post = self.tail

    # pop from the beginning
    def DL_popleft(self) -> DL_list:
        first_node = self.head.post
        self.head.post = first_node.post
        first_node.post.pre = self.head
        return first_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.DL_remove(node)
            self.DL_append(node)
            return node.value
        else:
            return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.DL_remove(node)
        elif len(self.cache) == self.size:
            node = self.DL_popleft()
            del self.cache[node.key]
        node = DL_list(key, value)
        self.DL_append(node)
        self.cache[key] = node

# fast method, Python ordered dictionary (implemented by double linked list)
# it uses collections.OrderedDict ojbection two functions:
# move_to_end(key, last=True), and popitem(last=True)
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  
        elif len(self.cache) == self.size:
            self.cache.popitem(last=False)
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 10)
obj.put(2, 20)
print(obj.get(1))
obj.put(1, 100)
print(obj.get(1))
obj.put(3, 30)
print(obj.get(2))
obj.put(4, 40)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))