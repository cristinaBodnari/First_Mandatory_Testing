from CristinaCode.KEANet import Purchase
import unittest


class Increment_Decrement_UnitTesting(unittest.TestCase):

    # Testing basic functionality of the increment_phone_Lines() function
    #########################################################
    def test_price_after_increment_cell_lines(self):
        test = Purchase()
        self.assertEqual(test.increment_phone_Lines(), 150)

    def test_price_max_8_cell_lines(self):
        test = Purchase()
        for i in range(0, 8):
            test.increment_phone_Lines()
        self.assertNotEqual(test.increment_phone_Lines(), 1350)

    def test__phone_lines(self):
        test = Purchase()
        test.increment_phone_Lines()
        self.assertEqual(test.phone_Lines, 1)

    def test_max_8_phone_lines(self):
        test = Purchase()
        for i in range(0, 8):
            test.increment_phone_Lines()
        self.assertNotEqual(test.phone_Lines, 9)
    #######################################################

    # Testing basic functionality of the decrement_phone_Lines() function
    #########################################################
    def test_price_after_decrement_cell_lines(self):
        test = Purchase()
        test.increment_phone_Lines()
        test.increment_phone_Lines()
        self.assertEqual(test.decrement_phone_Lines(), 150)

    def test_price_min_0_phone_lines(self):
        test = Purchase()
        self.assertNotEqual(test.decrement_phone_Lines(), -150)

    def test_min_0_phone_lines(self):
        test = Purchase()
        test.decrement_phone_Lines()
        self.assertNotEqual(test.phone_Lines, -1)
    #######################################################



