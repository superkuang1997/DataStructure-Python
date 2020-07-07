"""最多保存11个数据项"""

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:  # 散列冲突
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] is not None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)
                if self.slots[nextslot] is None:  # 找到空槽
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # 替代

    def get(self, key):
        startslot = self.hashfunction(key)
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, data):
        return self.put(key, data)

    def __len__(self):
        return len([x for x in self.slots if x is not None])

    def __contains__(self, item):
        return item in self.slots

    def describe(self):
        print(self.slots)
        print(self.data)

H = HashTable()
H[20] = 13
H[21] = 14
H[31] = 20
H[31] = 21
print(H[20])
print(H[21])
print(H[31])
print(len(H))
print(31 in H)
H.describe()