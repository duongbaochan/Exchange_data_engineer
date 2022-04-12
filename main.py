class Order:
    def __init__(self, order_id, add_side, add_price, add_qty, time):
        self.order_id = order_id
        self.add_side= add_side
        self.add_price= add_price
        self.add_qty = add_qty
        self.time = time

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # insert an element to the queue
    def enqueue(self, data):
        if (data.add_side == 'BUY'):
            pass
    # pop an element
    def dequeue(self):
        pass

    