#! /usr/bin/env python3

class hash_table():
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hash_func(key,self.size)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nexthashvalue = self.next_hash_func(hashvalue, self.size)
                found = False
                stop = False
                while self.slots[nexthashvalue] != None and not found and not stop:
                    if self.slots[nexthashvalue] == key:
                        found = True
                    elif hashvalue == nexthashvalue:
                        stop = True
                    else:
                        nexthashvalue = self.next_hash_func(nexthashvalue, self.size)
                if not stop:
                    self.slots[nexthashvalue] = key
                    self.data[nexthashvalue] = data
                else:
                    raise ValueError

    def hash_func(self, key, size):
        return key % size

    def next_hash_value(self, key, size):
        return (key + 1) % size

    def get(self, key):
        hashvalue = self.hash_func(key, self.size)
        if self.slots[hashvalue] == key:
            return self.data[hashvalue]
        else:
            nexthashvalue = self.next_hash_value(hashvalue, self.size)
            found = False
            stop = False
            while self.slots[nexthashvalue] != key and not stop:
                if nexthashvalue == hashvalue:
                    stop = True
                else:
                    nexthashvalue = self.next_hash_value(nexthashvalue, self.size)
            if not stop:
                return self.data[nexthashvalue]
            else:
                return None

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)


                    
