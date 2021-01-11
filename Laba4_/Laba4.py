from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium

def parse(url):
        
        driver = r'C:\Users\Alexey\Desktop\chromedriver.exe'
        browser = webdriver.Chrome(driver)
        browser.set_window_position(-10000,0)
        browser.get(url)
        sen = browser.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        browser.quit()
        return float(sen.replace(',','.'))

class abstarctconvert():

    def __init__(self, number):
        pass

    def convert(self):
        pass


class Converter(abstarctconvert):


    def __init__(self, valut):
        self.valut = valut

    def convert(self):
        ext = self.valut
        print(ext)
        if ext in ['доллар', 'Dollars']:
            el = parse('https://www.google.com/search?q=dollars&oq=dollars&aqs=chrome..69i57j0l7.30739j1j7&sourceid=chrome&ie=UTF-8')
            return 'Стоимость доллара в рублях: '+str(el)
        if ext in ['евро', 'Euro']:
            el = parse('https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE&oq=%D0%B5%D0%B2%D1%80%D0%BE&aqs=chrome..69i57j0i433l4j0j0i131i433j69i61.5487j1j7&sourceid=chrome&ie=UTF-8')
            return 'Стоимость евро в рублях: '+str(el)
        if ext in ['фунты','Paunt']:
            el = parse('https://www.google.com/search?q=%D1%84%D1%83%D0%BD%D1%82%D1%8B+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&oq=%D1%84%D1%83%D0%BD%D1%82&aqs=chrome.1.69i57j0i433j0i20i263j0i433l2j0j0i433j0.7465j0j7&sourceid=chrome&ie=UTF-8')
            return 'Стоимость фунта в рублях: ' + str(el)
        else:
            return 'Незнакомая валюта'


class Out:

    def __init__(self, sum_, data=abstarctconvert):
        self.sum_ = sum_
        self.data = data

    def Web_out(self):
        decoded = self.data.convert()
        if 'Незнакомая валюта' == decoded:
            return f' {decoded}'
        else:
            conver_sum =  int(float(self.sum_)*float(decoded.split(': ')[1]))
            return f' {decoded}, Наша сумма составляет: {conver_sum}'


class BankoMat:

    def __init__(self, name):
        self.name = name
        print(f"Вас приветствует банкомат {name}")

    def payment_of_the_money(self, sum_, name_valut):
        money = Out(sum_, data=Converter(name_valut))
        print(f'{self.name}:', money.Web_out())


if __name__ == '__main__':
    bnk = BankoMat('Сберанк')
    bnk.payment_of_the_money(1000,'доллар')
    bnk.payment_of_the_money(300,'евро')
    bnk.payment_of_the_money(500,'фунты')
    bnk.payment_of_the_money(500,'Тенге')
    
    
