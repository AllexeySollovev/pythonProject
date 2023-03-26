class Employ:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

class ProductionWorker(Employ):
    def __init__(self, name, phone, shiftnumber, rate):
        Employ.__init__(self, name, phone)
        if shiftnumber == 1.0:
            self.__shiftnumber = 'Дневная'
        elif shiftnumber == 2.0:
            self.__shiftnumber = 'Ночная'
        else:
            self.__shiftnumber = 'Не указано'
        self.__rate = rate

    def set_shiftnumber(self, shiftnumber):
        self.__shiftnumber = shiftnumber
    def set_rate(self, rate):
        self.__rate = rate

    def get_shiftnumber(self):
        return self.__shiftnumber

    def get_rate(self):
        return self.__rate
