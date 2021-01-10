# -*- coding: utf-8 -*-
"""
  Лабораторная работа 2
  Работа с файлом, необходимо выполнить операции с текстовым файлом 
  Стратегия, шаблонный метод
"""
import os
import shutil
file = 'C:/Users/Alexey/Desktop/file.txt'

class Delete_FILE:#Класс Операции
    def solve(self, file): 
        os.remove(file)
        return 'Файл - '+file+' успешно удален !'

class Copy_FILE:#Класс Операции
    def solve(self, file):
     shutil.copyfile(file,'C:/Users/Alexey/Desktop/сюда/'+file.split('/')[-1])
     return 'Файл успешно скопирован !'
 
class Create_FILE:#Класс Операции
    def solve(self, file):
        f = open(file, 'w', encoding = 'utf-8')
        f.close()
        return 'Файл - '+file+' успешно создан !'
     
class GENERAL: #Основной Класс
    def SET_STRATEGY(self, STRATEGY):
        self.STRATEGY = STRATEGY
        
    def solve(self, file):
        print(self.STRATEGY.solve(file))

        
start = GENERAL()

start.SET_STRATEGY(Delete_FILE())
start.solve("C:/Users/Alexey/Desktop/file.txt")
input()
start.SET_STRATEGY(Create_FILE())
start.solve("C:/Users/Alexey/Desktop/file.txt")
input()
start.SET_STRATEGY(Copy_FILE())
start.solve("C:/Users/Alexey/Desktop/file.txt")
input()
start.SET_STRATEGY(Delete_FILE())
start.solve("C:/Users/Alexey/Desktop/сюда/file.txt")