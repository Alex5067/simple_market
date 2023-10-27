class OrderBook:
    def __init__(self):
        self.buy_orders = {}
        self.sell_orders = {}

    def add_order(self, order):
        if order.type == 'buy':
            self.buy_orders[order.order_id] = order
        elif order.type == 'sell':
            self.sell_orders[order.order_id] = order

    def remove_order(self, order_id):
        if order_id in self.buy_orders:
            del self.buy_orders[order_id]
        elif order_id in self.sell_orders:
            del self.sell_orders[order_id]
        else:
            print(f"Order with order_id {order_id} not found in the order book.")

    def modify_order(self, order_id, new_quantity, new_price):
        order = self.buy_orders.get(order_id) or self.sell_orders.get(order_id)
        if order:
            order.quantity = new_quantity
            order.price = new_price
        else:
            print(f"Order with order_id {order_id} not found in the order book.")


    #Сопоставление
    def match_orders(self):
        buy_orders = sorted(self.buy_orders.values(), key=lambda x: x.price, reverse=True)
        sell_orders = sorted(self.sell_orders.values(), key=lambda x: x.price)

        while buy_orders and sell_orders:
            buy_order = buy_orders[0]
            sell_order = sell_orders[0]

            if buy_order.price >= sell_order.price:
                quantity_traded = min(buy_order.quantity, sell_order.quantity)

                print(f"Trade executed - Price: {sell_order.price}, Quantity: {quantity_traded}")
                buy_order.quantity -= quantity_traded
                sell_order.quantity -= quantity_traded

                if buy_order.quantity == 0:
                    del self.buy_orders[buy_order.order_id]
                if sell_order.quantity == 0:
                    del self.sell_orders[sell_order.order_id]
                # Пересортировка, чтобы учесть изменения в количестве
                buy_orders = sorted(self.buy_orders.values(), key=lambda x: x.price, reverse=True)
                sell_orders = sorted(self.sell_orders.values(), key=lambda x: x.price)
            else:
                break





