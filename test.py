import unittest
from Order import Order
from OrderBook import OrderBook

class TestOrder(unittest.TestCase):

    def test_order_creation(self):
        order = Order(order_id=1, timestamp=1635300000, order_type='buy', quantity=10, price=100)
        self.assertEqual(order.order_id, 1)
        self.assertEqual(order.timestamp, 1635300000)
        self.assertEqual(order.type, 'buy')
        self.assertEqual(order.quantity, 10)
        self.assertEqual(order.price, 100)

    def test_order_modification(self):
        order = Order(order_id=1, timestamp=1635300000, order_type='buy', quantity=10, price=100)
        order.quantity = 5
        order.price = 90
        self.assertEqual(order.quantity, 5)
        self.assertEqual(order.price, 90)

class TestOrderBook(unittest.TestCase):

    def setUp(self):
        self.order_book = OrderBook()

    def test_add_order(self):
        order = Order(order_id=1, timestamp=1635300000, order_type='buy', quantity=10, price=100)
        self.order_book.add_order(order)
        self.assertIn(1, self.order_book.buy_orders)

    def test_remove_order(self):
        order = Order(order_id=1, timestamp=1635300000, order_type='buy', quantity=10, price=100)
        self.order_book.add_order(order)
        self.order_book.remove_order(1)
        self.assertNotIn(1, self.order_book.buy_orders)

    def test_modify_order(self):
        order = Order(order_id=1, timestamp=1635300000, order_type='buy', quantity=10, price=100)
        self.order_book.add_order(order)
        self.order_book.modify_order(1, new_quantity=5, new_price=90)
        self.assertEqual(order.quantity, 5)
        self.assertEqual(order.price, 90)

    def test_match_orders(self):
        buy_order = Order(order_id=1, timestamp=1635300000, order_type='buy', quantity=10, price=100)
        sell_order = Order(order_id=2, timestamp=1635300001, order_type='sell', quantity=10, price=100)

        self.order_book.add_order(buy_order)
        self.order_book.add_order(sell_order)

        self.order_book.match_orders()

        self.assertNotIn(1, self.order_book.buy_orders)
        self.assertNotIn(2, self.order_book.sell_orders)

if __name__ == '__main__':
    unittest.main()
