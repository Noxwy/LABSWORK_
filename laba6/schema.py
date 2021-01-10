graph = {'0':[('lin0_1','1'),('lin0_12','12'),('lin0_11','11'),('lin0_10','10')],
          '1':[('lin1_7','7'),('lin1_0','0')],
          '2':[('lin2_6','6')],
          '3':[('lin3_11','11')],
          '4':[('lin4_10','10'),('lin4_6','6')],
          '5':[('lin5_8','8'),('lin5_13','13')],
          '6':[('lin6_10','10'),('lin6_4','4')],
          '7':[('lin7_13','13'),('lin7_1','1')],
          '8':[('lin8_12','12'),('lin8_5','5')],
          '9':[('lin9_11','11')],
          '10':[('lin10_6','6'),('lin10_4','4'),('lin10_0','0')],
          '11':[('lin11_12','12'),('lin11_14','14'),('lin11_9','9'),('lin11_3','3'),('lin11_0','0')],
          '12':[('lin12_11','11'),('lin12_0','0'),('lin12_8','8')],
          '13':[('lin13_7','7'),('lin13_5','5')],
          '14':[('lin14_11','11')]
          }
# graph = {

#     # Line 1
#     "Комсомольская (1)": [(6, "Комсомольская (5)"), (3, "Красные Ворота (1)")],
#     "Красные Ворота (1)": [(3, "Комсомольская (1)"), (3, "Чистые пруды (1)")],
#     "Чистые пруды (1)": [(3, "Красные Ворота (1)"), (3, "Тургеневская (6)"), (3, "Сретенский бульвар (10)"), (3, "Лубянка (1)")],
#     "Лубянка (1)": [(3, "Чистые пруды (1)"), (3, "Кузнецкий Мост (7)"), (3, "Охотный Ряд (1)")],
#     "Охотный Ряд (1)": [(3, "Лубянка (1)"), (4, "Театральная (2)"), (3, "Библиотека имени Ленина (1)")],
#     "Библиотека имени Ленина (1)":[(3, "Охотный Ряд (1)"), (3, "Александровский сад (4)"), (5, "Арбатская (3)"), (6, "Боровицкая (9)"), (3, "Кропоткинская (1)")],
#     "Кропоткинская (1)": [(3, "Библиотека имени Ленина (1)"), (3, "Парк культуры (1)")],
#     "Парк культуры (1)": [(3, "Кропоткинская (1)"), (5, "Парк культуры (5)")],

#     # Line 2
#     "Павелецкая (2)": [(4, "Павелецкая (5)"), (3, "Новокузнецкая (2)")],
#     "Новокузнецкая (2)": [(3, "Павелецкая (2)"), (3, "Третьяковская (8)"), (3, "Третьяковская (6)"), (4, "Театральная (2)")],
#     "Театральная (2)": [(4, "Новокузнецкая (2)"), (4, "Охотный Ряд (1)"), (5, "Площадь Революции (3)"), (3, "Тверская (2)")],
#     "Тверская (2)": [(3, "Театральная (2)"), (3, "Пушкинская (7)"), (4, "Чеховская (9)"), (3, "Маяковская (2)")],
#     "Маяковская (2)": [(3, "Тверская (2)"), (3, "Белорусская (2)")],
#     "Белорусская (2)": [(3, "Маяковская (2)"), (3, "Белорусская (5)")],

#     # Line 3
#     "Курская (3)": [(4, "Чкаловская (10)"), (4, "Курская (5)"), (4, "Площадь Революции (3)")],
#     "Площадь Революции (3)": [(4, "Курская (3)"), (5, "Театральная (2)"), (3, "Арбатская (3)")],
#     "Арбатская (3)": [(3, "Площадь Революции (3)"), (3, "Александровский сад (4)"), (5, "Библиотека имени Ленина (1)"), (3, "Боровицкая (9)"), (5, "Киевская (3)")],
#     "Киевская (3)": [(5, "Арбатская (3)"), (3, "Киевская (5)"), (5, "Киевская (4)")],

#     # Line 4
#     "Александровский сад (4)": [(3, "Библиотека имени Ленина (1)"), (3, "Арбатская (3)"), (4, "Арбатская (4)")],
#     "Арбатская (4)": [(4, "Александровский сад (4)"), (4, "Смоленская (4)")],
#     "Смоленская (4)": [(4, "Арбатская (4)"), (5, "Киевская (4)")],
#     "Киевская (4)": [(5, "Смоленская (4)"), (6, "Киевская (5)"), (5, "Киевская (3)")],

#     # Line 5
#     "Комсомольская (5)": [(4, "Проспект Мира (5)"), (6, "Комсомольская (1)"), (4, "Курская (5)")],
#     "Курская (5)": [(4, "Комсомольская (5)"), (4, "Курская (3)"), (6, "Чкаловская (10)"), (4, "Таганская (5)")],
#     "Таганская (5)": [(4, "Курская (5)"), (3, "Таганская (7)"), (3, "Марксистская (8)"), (3, "Павелецкая (5)")],
#     "Павелецкая (5)": [(3, "Таганская (5)"), (4, "Павелецкая (2)"), (3, "Добрынинская (5)")],
#     "Добрынинская (5)": [(3, "Павелецкая (5)"), (3, "Серпуховская (9)"), (3, "Октябрьская (5)")],
#     "Октябрьская (5)": [(3, "Добрынинская (5)"), (3, "Октябрьская (6)"), (3, "Парк культуры (5)")],
#     "Парк культуры (5)": [(3, "Октябрьская (5)"), (5, "Парк культуры (1)"), (4, "Киевская (5)")],
#     "Киевская (5)": [(4, "Парк культуры (5)"), (3, "Киевская (3)"), (6, "Киевская (4)"), (4, "Краснопресненская (5)")],
#     "Краснопресненская (5)": [(4, "Киевская (5)"), (3, "Баррикадная (7)"), (4, "Белорусская (5)")],
#     "Белорусская (5)": [(4, "Краснопресненская (5)"), (3, "Белорусская (2)"), (3, "Новослободская (5)")],
#     "Новослободская (5)": [(3, "Белорусская (5)"), (3, "Менделеевская (9)"), (4, "Проспект Мира (5)")],
#     "Проспект Мира (5)": [(4, "Новослободская (5)"), (4, "Проспект Мира (6)"), (4, "Комсомольская (5)")],

#     # Line 6
#     "Октябрьская (6)": [(3, "Октябрьская (5)"), (4, "Третьяковская (6)")],
#     "Третьяковская (6)": [(4, "Октябрьская (6)"), (2, "Третьяковская (8)"), (3, "Новокузнецкая (2)"), (4, "Китай-город (6)")],
#     "Китай-город (6)": [(4, "Третьяковская (6)"), (2, "Китай-город (7)"), (3, "Тургеневская (6)")],
#     "Тургеневская (6)": [(3, "Китай-город (6)"), (3, "Сретенский бульвар (10)"), (3, "Чистые пруды (1)"), (3, "Сухаревская (6)")],
#     "Сухаревская (6)": [(3, "Тургеневская (6)"), (3, "Проспект Мира (6)")],
#     "Проспект Мира (6)": [(3, "Сухаревская (6)"), (4, "Проспект Мира (5)")],

#     # Line 7
#     "Таганская (7)": [(3, "Таганская (5)"), (4, "Марксистская (8)"), (4, "Китай-город (7)")],
#     "Китай-город (7)": [(4, "Таганская (7)"), (2, "Китай-город (6)"), (3, "Кузнецкий Мост (7)")],
#     "Кузнецкий Мост (7)": [(3, "Китай-город (7)"), (3, "Лубянка (1)"), (3, "Пушкинская (7)")],
#     "Пушкинская (7)": [(3, "Кузнецкий Мост (7)"), (3, "Тверская (2)"), (4, "Чеховская (9)"), (4, "Баррикадная (7)")],
#     "Баррикадная (7)": [(4, "Пушкинская (7)"), (3, "Краснопресненская (5)")],

#     # Line 8
#     "Марксистская (8)": [(4, "Таганская (7)"), (3, "Таганская (5)"), (4, "Третьяковская (8)")],
#     "Третьяковская (8)": [(4, "Марксистская (8)"), (3, "Новокузнецкая (2)"), (2, "Третьяковская (6)")],

#     # Line 9
#     "Серпуховская (9)": [(3, "Добрынинская (5)"), (3, "Полянка (9)")],
#     "Полянка (9)": [(3, "Серпуховская (9)"), (3, "Боровицкая (9)")],
#     "Боровицкая (9)": [(3, "Полянка (9)"), (6, "Библиотека имени Ленина (1)"), (3, "Арбатская (3)"), (4, "Чеховская (9)")],
#     "Чеховская (9)": [(4, "Боровицкая (9)"), (4, "Пушкинская (7)"), (4, "Тверская (2)"), (3, "Цветной бульвар (9)")],
#     "Цветной бульвар (9)": [(3, "Чеховская (9)"), (4, "Трубная (10)"), (4, "Менделеевская (9)")],
#     "Менделеевская (9)": [(4, "Цветной бульвар (9)"), (3, "Новослободская (5)")],

#     # Line 10
#     "Чкаловская (10)": [(6, "Курская (5)"), (4, "Курская (3)"), (4, "Сретенский бульвар (10)")],
#     "Сретенский бульвар (10)": [(4, "Чкаловская (10)"), (3, "Тургеневская (6)"), (3, "Чистые пруды (1)"), (4, "Трубная (10)")],
#     "Трубная (10)": [(4, "Сретенский бульвар (10)"), (4, "Цветной бульвар (9)")],

# }