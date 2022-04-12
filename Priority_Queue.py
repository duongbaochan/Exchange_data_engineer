'''
    Priority queue
'''

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # heapify for enqueue
    def enqueueHeapify(self, s, compare):
        if s == 0:
            return
        parent = (s-1)//2
        if compare(self.queue[s], self.queue[parent]) > 0:
            c = self.queue[s]
            self.queue[s] = self.queue[parent]
            self.queue[parent] = c
            self.enqueueHeapify(parent, compare)

    # insert an element to the queue
    def enqueue(self, data, compare):
        self.queue.append(data)
        s = len(self.queue) - 1
        self.enqueueHeapify(s, compare)
    
    # heapify for dequeue
    def dequeueHeapify(self, s, compare):
        left = 2 * s + 1
        right = 2 * s + 2
        largest = s
        if left < len(self.queue):
            if compare(self.queue[left], self.queue[s]) > 0:
                largest = left

        if right < len(self.queue):
            if compare(self.queue[right], self.queue[s]) > 0:
                largest = right

        if largest != s:
            c = self.queue[s]
            self.queue[s] = self.queue[largest]
            self.queue[largest] = c
            self.dequeueHeapify(largest, compare)

    
    # pop an element from queue
    def dequeue(self, compare):
        s = len(self.queue) - 1
        c = self.queue[s]
        self.queue[s] = self.queue[0]
        self.queue[0] = c
        res = self.queue.pop()
        self.dequeueHeapify(0, compare)
        return res