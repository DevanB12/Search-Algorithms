import random
import time

def sequentialSearch(alist, item):
    pos = 0
    found  = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found

def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint+1:], item)

class HashTable:
    def __init__(self, size, loadFactor):
        self.size = size * int((1/loadFactor))
        self.slots = [None] * self.size

    def hashfunction(self, item):
        return item%self.size

    def rehash(self, oldhash):
        return (oldhash + 3) % self.size

    def store(self, item):
        hashvalue = self.hashfunction(item)
        
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = item
        else:
            nextslots = self.rehash(hashvalue)
            while self.slots[nextslots] != None:
                nextslots = self.rehash(nextslots)

            self.slots[nextslots] = item

    def search(self, data):
        hashValue = self.hashfunction(data)
        found = False
        if self.slots[hashValue] == data:
            found = True
            return found

        else:
            nextslots = self.rehash(hashValue)
            while self.slots[nextslots] != None and found == False:
                nextslots = self.rehash(nextslots)
                if self.slots[nextslots] == data:
                    found = True
            return found

    def QuickLoad(self, listvals):
        #self.size = int((1/loadFactor))
        #self.slots = [None]*self.size
        for i in listvals:
            self.store(i)
        

def seqTest():
    timeAvg = 0
    alist = []
    for listSize in range(10000, 100001, 10000):
        #alist = random.sample(range(100000), listSize)
        for i in range(0, listSize):
            alist.append(i)
        for c in range(0, 10):
            start = time.time()
            sequentialSearch(alist, listSize-1)
            end = time.time()
            timeTotal = end - start
            timeAvg = timeAvg + timeTotal
        print('It took', timeAvg/10, 'seconds on average for', listSize, 'number of items.')
        

def binaryTest():
    timeAvg = 0
    alist = []
    for listSize in range(10000, 100001, 10000):
        for i in range(0, listSize):
            alist.append(i)
        for i in range(0, 10):
            start = time.time()
            binarySearch(alist, listSize-1)
            end = time.time()
            timeTotal = end - start
            timeAvg = timeAvg + timeTotal
        print('It took', timeAvg/10, 'seconds on average for', listSize, 'number of items.')

def htTest():
    timeAvg = 0
    alist = []
    for listSize in range(10000, 100001, 10000):
        for l in range(0, 10):
            ht = HashTable(listSize, .5)
            #for i in random.sample(range(100000), listSize):
                #ht.store(i)
            ht.QuickLoad(random.sample(range(1000000), listSize))
            start = time.time()
            ht.search(100000000)
            end = time.time()
            timeTotal = end - start
            timeAvg = timeAvg + timeTotal
        print('It took', timeAvg/10, 'seconds on average for', listSize, 'number of items.')

#seqTest()
#binaryTest()
#htTest()
