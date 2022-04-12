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
    else:
        if x.add_price > y.add_price:
            return -1
        elif x.add_price < y.add_price:
            return 1
        else:
            if x.seq_num < y.seq_num:
                return 1
            elif x.seq_num > y.seq_num:
                return -1
    return 0