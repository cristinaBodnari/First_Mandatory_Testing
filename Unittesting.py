from KEANet import Purchase
import unittest


class Increment_Decrement_UnitTesting(unittest.TestCase):
    # Testing the internet conection function
    def test_select_internet_connection1(self):
        test = Purchase()
        self.assertEqual(test.internet_Connections(True), 200)

    def test_select_internet_connection2(self):
        test = Purchase()
        self.assertEqual(test.internet_Connections(False), -200)
        
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

    #Test if the correct price is return
    def test_price_after_increment_cell_lines(self):
        test = Purchase()
        self.assertEqual(test.increment_phone_Lines(), 150)

    #Test if the price is stop increasing if the limit of 8 cell lines is reached
    def test_price_max_8_cell_lines(self):
        test = Purchase()
        for i in range(0, 8):
            test.increment_phone_Lines()
        self.assertNotEqual(test.increment_phone_Lines(), 1350)

    #test if phone_lines is corectly increasing when calling the increment_phone_Lines() method
    def test__phone_lines(self):
        test = Purchase()
        test.increment_phone_Lines()
        self.assertEqual(test.phone_Lines, 1)

    ##Test if the phone_lines stops increasing when the limit is reached
    def test_max_8_phone_lines(self):
        test = Purchase()
        for i in range(0, 8):
            test.increment_phone_Lines()
        self.assertNotEqual(test.phone_Lines, 9)
    #######################################################

    # Testing basic functionality of the decrement_phone_Lines() function
    #########################################################

    #Test if the function is return the corect price
    def test_price_after_decrement_cell_lines(self):
        test = Purchase()
        test.increment_phone_Lines()
        test.increment_phone_Lines()
        self.assertEqual(test.decrement_phone_Lines(), 150)

    #Test if the function doesn't decrease the price if the function is called with unexisting phone line
    def test_price_min_0_phone_lines(self):
        test = Purchase()
        self.assertNotEqual(test.decrement_phone_Lines(), -150)

    #Test if the function doesn't decrease unexisting phone lines
    def test_min_0_phone_lines(self):
        test = Purchase()
        test.decrement_phone_Lines()
        self.assertNotEqual(test.phone_Lines, -1)
    #######################################################

###########
