import unittest
from pizza import Pizza


class TestDominos(unittest.TestCase):
    def setup(self):
        pass

    def test_without_args(self):
        '''
        order1 = Pizza()
        order1.get_bill()
        124
        '''
        order1 = Pizza()
        self.assertEqual(order1.get_bill(), 124)

    def test_large_with_0(self):
        '''
        order2 = Pizza('large', 0)
        order2.get_bill()
        '''
        order2 = Pizza('large', 0)
        self.assertEqual(order2.get_bill(), 0)

    def test_regular_with_4(self):
        '''
        order3 = Pizza('regular', 4)
        order3.get_bill()
        '''
        order3 = Pizza('regular', 4)
        self.assertEqual(order3.get_bill(), 992)


if __name__ == '__main__':
    unittest.main()

