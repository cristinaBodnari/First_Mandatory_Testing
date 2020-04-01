class Purchase:

    def __init__(self):
        self.internet_Connection = False
        self.phone_Lines = 0
        self.cell_Phones = ['Motorola G99', 'iPhone 99', 'Samsung Galaxy 99', 'Sony Xperia 99', 'Huawei 99']
        self.price = 0

    def internet_Connections(self, user_Choices):
        if user_Choices:
            self.price += 200
            self.internet_Connection = True
        else:
            self.price -= 200
            self.internet_Connection = False

        return self.price

    def increment_phone_Lines(self):
        if self.phone_Lines < 8:
            self.price += 150
            self.phone_Lines +=1
        return self.price

    def decrement_phone_Lines(self):
        if self.phone_Lines >0:
            self.price -= 150
            self.phone_Lines -=1
        return self.price

    def select_cell_phone(self,phone):
        cell_prices = [800,6000,1000,900,900]
        dictionary = dict(zip(self.cell_Phones, cell_prices))
        for cell in dictionary:
            if phone == cell:
                self.price +=dictionary.get(cell)
        return self.price

    def unselect_cell_phone(self,phone):
        cell_prices = [800,6000,1000,900,900]
        dictionary = dict(zip(self.cell_Phones, cell_prices))
        for cell in dictionary:
            if phone == cell:
                self.price -=dictionary.get(cell)
        return self.price

    def buy(self):
        if self.price == 0:
            try:
                print()
            except ValueError:
                print("Please add something to the list")













