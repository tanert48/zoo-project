import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    #ECP
    def test_1_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_2_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_3_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)    

    def test_4_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 'invalid')
    
    def test_5_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    def test_6_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    #BVA
    def test_7_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 'invalid')
    def test_8_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    def test_9_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
    def test_10_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
    def test_11_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
    def test_12_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    def test_13_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
    def test_14_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
    def test_15_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(90), 100)
    def test_16_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(91), 100)
    

if __name__ == '__main__':
    unittest.main()