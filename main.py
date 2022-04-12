import queue


class Order:
    def __init__(self,seq_num, order_id, add_side, add_price, add_qty, time):
        self.seq_num = seq_num
        self.order_id = order_id
        self.add_side= add_side
        self.add_price= add_price
        self.add_qty = add_qty
        self.time = time

# compare two orders x and y
def compareOrder(x, y):
    if x.add_side != y.add_side:
        return -2
    if x.add_side == "BUY":
        if x.add_price > y.add_price:
            return 1
        elif x.add_price < y.add_price:
            return -1
        else:
            if x.seq_num < y.seq_num:
                return 1
            elif x.seq_num > y.seq_num:
                return -1
    return 0

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
        s = self.queue.__len__() - 1
        self.enqueueHeapify(s, compare)
    
    # heapify for dequeue
    def dequeueHeapify(self, s, compare):
        left = 2 * s + 1
        right = 2 * s + 2
        largest = s
        if left < self.queue.__len__():
            if compare(self.queue[left], self.queue[s]) > 0:
                largest = left

        if right < self.queue.__len__():
            if compare(self.queue[right], self.queue[s]) > 0:
                largest = right

        if largest != s:
            c = self.queue[s]
            self.queue[s] = self.queue[largest]
            self.queue[largest] = c
            self.dequeueHeapify(largest, compare)

    
    # pop an element from queue
    def dequeue(self, compare):
        s = self.queue.__len__() - 1
        c = self.queue[s]
        self.queue[s] = self.queue[0]
        self.queue[0] = c
        res = self.queue.pop()
        self.dequeueHeapify(0, compare)
        return res

