#=---Абстрактная фабрика и строитель---------
class Shop:

    def get_fish(self):
        pass
    
    def get_rise(self):
        pass
    
    def get_Cucumber(self):
        pass
    
    def get_cheeze(self):
        pass
    
    def get_souce(self):
        pass

        
class Fish_dish():

    def __init__(self):
        self.name = ''
        self.solt = ''
    def __str__(self):
        return f'{self.name } ({self.solt})'


class Sushi_fish(Fish_dish):

    def __init__(self):
        self.name = 'Лосось'
        self.solt = 'Слабосоленый'


class Course_fish(Fish_dish):
    
    def __init__(self):
        self.name = 'Дорадо'
        self.solt = 'Соленая'
        
class Rise_dish():
    
    def __init__(self):
        self.name = ''
    def __str__(self):
        return f'{self.name }'

class Sushi_rise(Rise_dish):

    def __init__(self):
        self.name = 'Белый '


class Course_rise(Rise_dish):

    def __init__(self):
        self.name = 'Коричневый рис'

class Cucumber_dish():
    
    def __init__(self):
        self.name = ''
    def __str__(self):
        return f'{self.name }'

class Sushi_Cucumber(Cucumber_dish):

    def __init__(self):
        self.name = 'Средний огурец'


class Course_Cucumber(Cucumber_dish):

    def __init__(self):
        self.name = 'Длинный огурец'


class Cheeze_dish():
    
    def __init__(self):
        self.name = ''
    def __str__(self):
        return f'{self.name }'

class Sushi_cheeze(Cheeze_dish):

    def __init__(self):
        self.name = 'Сливочный'


class Course_cheeze(Cheeze_dish):

    def __init__(self):
        self.name = 'Сыр Российский'


class Souce_dish():
    
    def __init__(self):
        self.name = ''
    def __str__(self):
        return f'{self.name }'

class Sushi_souce(Souce_dish):

    def __init__(self):
        self.name = 'Соевый с вассаби'

class Course_souce(Souce_dish):

    def __init__(self):
        self.name = 'Соус Терияки'


class Azbuka_Vkusa(Shop):

    def get_fish(self):
        return Course_fish()
    
    def get_rise(self):
        return Course_rise()
    
    def get_Cucumber(self):
        return Course_Cucumber()
    
    def get_cheeze(self):
        return Course_cheeze()
    
    def get_souce(self):
        return Course_souce()



class Auchan(Shop):
    
    def get_fish(self):
        return Sushi_fish()
    
    def get_rise(self):
        return Sushi_rise()
    
    def get_Cucumber(self):
        return Sushi_Cucumber()
    
    def get_cheeze(self):
        return Sushi_cheeze()
    
    def get_souce(self):
        return Sushi_souce()

class Dish:

    def __init__(self):
        self.fish = ''
        self.rise = ''
        self.cucumber = ''
        self.cheeze = ''
        self.souce = ''
        self.cooking = ''
        self.serving = ''

    def __str__(self):
        return (
            'Блюдо:\n' +
            f'\tРыба: {self.fish}\n' +
            f'\tРис: {self.rise}\n' +
            f'\tОгурец: {self.cucumber}\n' +
            f'\tСыр: {self.cheeze}\n'+
            f'\tСоус: {self.souce}\n'+
            f'\tПриготовление: {self.cooking}\n'+
            f'\tСерверовка: {self.serving}\n'
        )


class Chef:

    def cook(self, shop):
        self.dish = Dish()
        self.shop = shop
#-----------------------------Отсюда менять------------------------------

class Plate(Chef):

   def set_fish(self):
        self.dish.fish = self.shop.get_fish()
       
   def set_rise(self):
        self.dish.rise = self.shop.get_rise()
    
   def set_Cucumber(self):
        self.dish.cucumber = self.shop.get_Cucumber()
    
   def set_cheeze(self):
       self.dish.cheeze = self.shop.get_cheeze()
    
   def set_souce(self):
        self.dish.souce = self.shop.get_souce()
        
   def set_cooking(self):
       self.dish.cooking = "Жарим рыбу с соусом и варим рис"
       
   def set_serving(self):
       self.dish.serving = "Выкладываем на блюдо вместе с рисом"
        

class Sushi_board(Chef):
    
   def set_fish(self):
        self.dish.fish = self.shop.get_fish()
       
   def set_rise(self):
        self.dish.rise = self.shop.get_rise()
    
   def set_Cucumber(self):
        self.dish.cucumber = self.shop.get_Cucumber()
    
   def set_cheeze(self):
       self.dish.cheeze = self.shop.get_cheeze()
    
   def set_souce(self):
        self.dish.souce = self.shop.get_souce()
        
   def set_cooking(self):
       self.dish.cooking = "Сворачиваем рол со всеми ингридиентами"
       
   def set_serving(self):
       self.dish.serving = "Выкладываем рол на тарелку и наливаем соус"


class Restaurant:

    def delivery(self, deliveryman):
        self.deliveryman = deliveryman

    def deliveryclub(self, shop):
        self.deliveryman.cook(shop)
        self.deliveryman.set_fish()
        self.deliveryman.set_rise()
        self.deliveryman.set_Cucumber()
        self.deliveryman.set_cheeze()
        self.deliveryman.set_souce()
        self.deliveryman.set_cooking()
        self.deliveryman.set_serving()
        return self.deliveryman.dish

if __name__ == '__main__':
    Res = Restaurant()
    Res.delivery(Sushi_board())
    c = Res.deliveryclub(Auchan())
    print(c)
