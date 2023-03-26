class Employee:
    def __init__(self, name, identification, section, post):
        self.__name = name
        self.__identification = identification
        self.__section = section
        self.__post = post

    def set_name(self, name):
        self.__name = name

    def set_identification(self, identification):
        self.__identification = identification

    def set_section(self, section):
        self.__section = section

    def set_post(self, post):
        self.__post = post

    def get_name(self):
        return self.__name

    def get_identification(self):
        return self.__identification

    def get_section(self):
        return self.__section

    def get_post(self):
        return self.__post
    def __str__(self):
        return f'{self.__name} {self.__identification} {self.__section} {self.__post}\n'
