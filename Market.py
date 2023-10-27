import random
import time
from Order import Order
from OrderBook import OrderBook

def simple_market(order_book, num_orders):
    #Имитация
    for i in range(num_orders):
        order_type = random.choice(['buy', 'sell'])
        quantity = random.randint(1, 10)
        price = random.randint(1, 1000)

        order = Order(order_id=i, timestamp=time.time(), order_type=order_type, quantity=quantity, price=price)

        order_book.add_order(order)
        print(f"Order placed - Type: {order.type}, Quantity: {order.quantity}, Price: {order.price}, ID: {order.order_id}")

        # Для периодического сопоставления
        if random.random() < 0.5:
            order_book.match_orders()

        # Проходит некоторое время до следующего заказа, для симуляции
        time.sleep(1)

if __name__ == '__main__':
    order_book = OrderBook()

    simple_market(order_book, 20)