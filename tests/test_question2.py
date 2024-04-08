import unittest

from src.question2 import Orders


class TestOrders(unittest.TestCase):
    def test_combine_orders(self):
        mock_orders = [70, 30, 10]
        mock_n_max = 100
        expected_orders = 2
        orders = Orders()

        how_many = orders.combine_orders(requests=mock_orders, n_max=mock_n_max)

        self.assertEqual(how_many, expected_orders)


if __name__ == '__main__':
    unittest.main()
