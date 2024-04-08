from src.question1 import Contract, Contracts
import unittest


class TestContracts(unittest.TestCase):
    def test_get_top_n_open_contracts(self):
        mock_contracts = [
            Contract(1, 1),
            Contract(2, 2),
            Contract(3, 3),
            Contract(4, 4),
            Contract(5, 5)
        ]
        mock_renegotiated = [3]
        mock_top_n = 3

        expected_open_contracts = [5, 4, 2]

        contracts = Contracts()
        actual_open_contracts = contracts.get_top_n_open_contracts(open_contracts=mock_contracts,
                                                                   renegotiated_contracts=mock_renegotiated,
                                                                   top_n=mock_top_n)

        self.assertEqual(expected_open_contracts, actual_open_contracts)


if __name__ == '__main__':
    unittest.main()
