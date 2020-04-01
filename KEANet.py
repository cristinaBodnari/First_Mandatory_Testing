class Purchase:

#aaaa
    def __init__(self):
        self.internet_Connection = False
        self.phone_Lines = 0
        self.cell_Phones = ['Motorola G99', 'iPhone 99', 'Samsung Galaxy 99', 'Sony Xperia 99', 'Huawei 99']
        self.price = 0
        self.list_of_phones =[]

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
                self.list_of_phones.append(phone)
        return self.price

    def unselect_cell_phone(self,phone):
        #sasj
        cell_prices = [800,6000,1000,900,900]
        dictionary = dict(zip(self.cell_Phones, cell_prices))
        for cell in dictionary:
            if phone == cell:
                self.price -=dictionary.get(cell)

                if  phone in self.list_of_phones:
                    self.list_of_phones.remove(phone)
        return self.price

    def buy(self):
        output =""
        if self.price == 0:
            output = "Please add something to the list"
        else:
            for i in self.list_of_phones:
                output += i + " "
        return output
