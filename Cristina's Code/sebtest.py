from KEANet import Purchase
import unittest

class TestMethods(unittest.TestCase):
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





unittest.main(verbosity = 3)