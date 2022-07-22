from binaryheap import BinHeap
import random


randList = []
for i in range(0,10):
    n = random.randint(1,100)
    randList.append(n)

print(randList)

heap = BinHeap()

for j in range(len(randList)):
    heap.insert(randList[j])
    print(heap.heapList)
 

heap2 = BinHeap()
heap2.buildHeap(randList)
print(heap2.heapList)

