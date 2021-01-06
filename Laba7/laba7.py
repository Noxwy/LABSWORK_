from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#------------------------------------------Посредник (Ощение с сервисом рандомного числа)---------------------------------

class Message:
    def translate_message(self):
        pass


class TranslateToInteger(Message):
    def __init__(self, text):
        self.text = text

    def translate_message(self):
        try:
            print('Преобразование из str в int для сложения!')
            print('Ваше число: '+str(int(self.text)+1))
        except Exception as e:
            print(e)


class TranslateToString(Message):
    def __init__(self, text):
        self.text = text

    def translate_message(self):
        try:
            print('Ваше число: '+self.text)
        except Exception as e:
            print(e)


class Translator:
    def __init__(self, source):
        self.source = source

    def translate(self):
        return self.source.translate_message()

class Mediator():
    def notify(self, sender, event):
        pass


class MessengerWixWebSite(Mediator):
    def __init__(self, client, robot):
        self._client = client
        self._client.mediator = self
        self._robot = robot
        self._robot.mediator = self

class User:
    def __init__(self, mediator=None):
        self.mediator = mediator


class Robot_Site(User):
    def send_message(self, text):
        print(f"Робот отправил сообщение: {text}")
    def processing_on_the_site(self, type_):
        url = 'https://randstuff.ru/number/'
        driver = r'C:\Users\Alexey\Desktop\chromedriver.exe'
        browser = webdriver.Chrome(driver)
        browser.set_window_position(-10000,0)
        browser.get(url)
        sen = browser.find_element_by_xpath('//*[@id="number-end"]')
        for i in range(1,4):
            sen.send_keys(Keys.BACKSPACE)
        sen.send_keys('1000')
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="button"]').click()
        time.sleep(2)
        result = browser.find_element_by_xpath('//*[@id="number"]/span').text
        print('Число: '+result)
        print('Тип: '+str(type(result)))
        browser.quit()
        if type_ == 'int':
            message = TranslateToInteger(result)
            Translator(message).translate()
            #self._robot.get_message(translated)
        elif type_ == 'str':
            message = TranslateToString(result)
            Translator(message).translate()
            #self._robot.get_message(translated)
    def get_message(self, text):
        print(f"Клиент получил сообщение от робота: {text}")


class Client(User):
    def send_message(self, text):
        print(f"Клиент отправил сообщение: {text}")
        #self.mediator.notify(self, "Seller to Buyer", text)

    def get_message(self, text):
        print(f"Робот получил сообщение: {text}")


if __name__ == "__main__":
    robot = Robot_Site()
    client = Client()
    messenger = MessengerWixWebSite(robot, client)
#-----------------------------Первый пример-----------------------------------------------
    client.send_message("Мне нужно получить число с сайта, прибавить его к 1 и вывести в консоль и тип данных!")
    robot.send_message("Добрый день! Сейчас выведу число и тип данных.")
    print('\t.....Загрузка.....')
    robot.processing_on_the_site('int') 
    print('\n')
#-----------------------------Второй пример-----------------------------------------------   
    client.send_message("Мне нужно получить число с сайта, и вывести в консоль и тип данных!")
    robot.send_message("Добрый день! Сейчас выведу число и тип данных.")
    print('\t.....Загрузка.....')
    robot.processing_on_the_site('str')