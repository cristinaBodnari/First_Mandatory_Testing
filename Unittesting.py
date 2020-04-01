from CristinaCode.KEANet import Purchase
import unittest


class Increment_Decrement_UnitTesting(unittest.TestCase):
    def test_select_cellphone(self):
        test = Purchase()
        self.assertEqual(test.select_cell_phone('Motorola G99'), 800)

    def test_select_cellphone1(self):
        test = Purchase()
        self.assertEqual(test.select_cell_phone('iPhone 99'), 6000)

    def test_select_cellphone2(self):
        test = Purchase()
        self.assertEqual(test.select_cell_phone('Samsung Galaxy 99'), 1000)

    def test_select_cellphone3(self):
        test = Purchase()
        self.assertEqual(test.select_cell_phone('Sony Xperia 99'), 900)

    def test_select_cellphone4(self):
        test = Purchase()
        self.assertEqual(test.select_cell_phone('Huawei 99'), 900)

    def test_unselect_cellphone(self):
        test = Purchase()
        self.assertEqual(test.unselect_cell_phone('Motorola G99'), -800)

    def test_unselect_cellphone1(self):
        test = Purchase()
        self.assertEqual(test.unselect_cell_phone('iPhone 99'), -6000)

    def test_unselect_cellphone2(self):
        test = Purchase()
        self.assertEqual(test.unselect_cell_phone('Samsung Galaxy 99'), -1000)

    def test_unselect_cellphone3(self):
        test = Purchase()
        self.assertEqual(test.unselect_cell_phone('Sony Xperia 99'), -900)

    def test_unselect_cellphone4(self):
        test = Purchase()
        self.assertEqual(test.unselect_cell_phone('Huawei 99'), -900)

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



