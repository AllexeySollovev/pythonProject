class Customer:
    def __init__(self, name, adress, phone):
        self.__name = name
        self.__adress = adress
        self.__phone = phone
    def set_name(self, name):
        self.__name = name
    def set_adress(self, adress):
        self.__adress = adress
    def set_phone(self, phone):
        self.__phone = phone
    def get_name(self):
        return self.__name
    def get_adress(self):
        return self.__adress
    def get_phone(self):
        return self.__phone

class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
    def set_make(self, make):
        self.__make = make
    def set_model(self, model):
        self.__model = model
    def set_year(self, year):
        self.__year = year
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
TAX = 0.05
class ServiceQuote:
    def __int__(self, parts_charges, labor_charges):
        self.__parts_charges = parts_charges
        self.__labor_charges = labor_charges
    def set_parts_charges(self, parts_charges):
        self.__parts_charges = parts_charges
    def set_labor_charges(self, labor_charges):
        self.__labor_charges = labor_charges
    def get_parts_charges(self):
        return self.__parts_charges
    def get_labor_charges(self):
        return self.__labor_charges
    def get_sales_tax(self):
        return self.__parts_charges * TAX
    def get_total_charges(self):
        return self.__parts_charges + self.__labor_charges + \
            self.__parts_charges * TAX

