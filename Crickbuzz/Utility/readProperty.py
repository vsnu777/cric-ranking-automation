import configparser

config = configparser.ConfigParser()
config.read("C:\\Users\\Vishnu\\PycharmProjects\\Crickbuzz\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        ApplicationUrl = config.get('ApplicationURL','Crickbuzz')
        return ApplicationUrl


