# -*- coding: utf-8 -*-
"""
Лабораторная работ 3
Выгодная постройка дома
Главным критерием является Цена и Срок гарантии.
Посититель, итератор
"""
import random

class FIND_COMPANY ():
    

    def visit_company(self, company):
         pass    
     
class Company():

    def __init__(self, Name):
        self.Name = Name
        self.timing = "---"
        self.price = "---"
        self.design = "---"
        self.warranty = random.choice(Warrianty)
        self.special_offer = random.choice(Offer)
        self.solve_variant = "---"

    def __str__(self):
        self.string = (f"Компания: {self.Name}\n" +
            f"Срок изготовления: {self.timing}\n" +
            f"Цена: {self.price}\n" + 
            f"Дизайн дома: {self.design}\n"+
            f"Гарантия: {self.warranty}\n"+
            f"Специальное предложение: {self.special_offer}\n")
        return self.string 

    def price__(self):
        self.price= round(random.uniform(3000000, 10000000), 0)
        print(f"Цена: {self.price}")
        
    def timing__(self):
        self.timing= round(random.uniform(1, 3), 0)
        print(f"Срок изготовления: {self.timing}")
        
    def design__(self):
        self.design= round(random.uniform(1, 10), 0)
        print(f"Дизайн дома: {self.design}")
        
    def accept(self, co=FIND_COMPANY ):
        print(f"Компания: {self.Name}")
        co.visit_site_company(self)
        
class shop_():

    def __init__(self, _names):
        self.company_names = []
        for name in _names:
            self.company_names.append(Company(name))
    
    def __str__(self):
        result = ''
        for company_ in self.company_names:
            result += str(company_) + "\n"
        return result[:-1]
    
    def accept(self, co=FIND_COMPANY):
        for com_ in self.company_names:
            com_.accept(co)
            
class first(FIND_COMPANY):

    def visit_site_company(self, attribute_company=Company):
        attribute_company.timing__()
        attribute_company.price__()
        attribute_company.design__()
        print('\n')
        
class create_house():
    
    def __init__(self, collection=[]):
        self.collection = collection
        self.cursor = 0

    def current(self):
        if self.cursor < len(self.collection):
            return self.collection[self.cursor]

    def next(self):
        if len(self.collection) >= self.cursor + 1:
            self.cursor += 1

    def has_next(self):
        has_lenght = len(self.collection) >= self.cursor + 1
        if not has_lenght: self.cursor = 0
        return has_lenght

    def add(self, item):
        self.collection.append(item)

class Find_best_choice(FIND_COMPANY):
    def visit_site_company(self, attribute_company=Company):
        if attribute_company.price<=9000000 and attribute_company.warranty >=5 :
            attribute_company.solve_variant = 'Да'
        else:
            attribute_company.solve_variant = 'Нет'
        print(f"Подходит ли данный вариант заказчику: {attribute_company.solve_variant}\n")
        
if __name__ == '__main__':   
    Offer = ['Скидка 70 % на внутреннюю отделку дома','Бесплатная доставка материалов','Постройка дровника в подарок']
    Warrianty = [3,5,10]
    ch = create_house()
    ch.add(shop_(['Наша Бригада','Домэкс', 'САУТГРУП','КРОСТ']))
    #Начали поиск пердложений
    print('\t--Начали поиск пердложений --')
    while ch.has_next():
        print(str(ch.current()))
        ch.next()
    fir = first()
    #Спустя 2 недели 
    print('\t--Спустя 2 недели --')
    while ch.has_next():
        ch.current().accept(fir)
        ch.next()
    print('\t--Полученные данные для постройки дома--')
    #Полученные данные для постройки дома
    while ch.has_next():
        print(str(ch.current()))
        ch.next()
    #Находим лучшйи вариант
    print('\t--Находим лучшйи вариант--')
    best = Find_best_choice()
    while ch.has_next():
        ch.current().accept(best)
        ch.next()
