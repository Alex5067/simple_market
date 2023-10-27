class Order:
    def __init__(self, order_id, timestamp, order_type, quantity, price):
        self.order_id = order_id
        self.timestamp = timestamp
        self.type = order_type
        self.quantity = quantity
        self.price = price
