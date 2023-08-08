# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько 
# легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  
# Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и 
# “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

# Метод решения: 
# 1. Фразы разделены пробелами, ищем. 
# 2. С помощью split() формуируем список слов. 
# 3. Цикл по списку, берём каждое слово и ищем количество 
# гласных (для примера возьмём только 'a', как в задаче), 
# c помощью условия or можно комбинировать любую комбинацию гласных.
# 4. Находим гласные с помощью встроенного метода count(), по 
# циклу сравниваем его с остальными словами в списке. 
# 5. Печатаем результат. 

# Сразу формируем список фраз Винни-Пуха. 
list_phrases = input('Винни, скажи что-нибудь: ').split(' '); 
# Счетчик надо инициализировать, чтобы там хранилось значение первой фразы, 
# чтобы сравнивать с ним остальные фразы через условие в цикле.
count = list_phrases[0].count('а')
# Инициализируем флаг, чтобы там отобразить результат проверок по циклу.
flag = False

for i in range (0, len(list_phrases)):
    # В условии надо учесть, что flag будет равен False , 
    # когда Винни ничего не сказал, или сказал лишь одну фразу. 
    if list_phrases[i].count('а') == count and len(list_phrases) > 1:
        flag = True
    else:
        flag = False

if flag:
    print('Парам пам-пам')
else:
    print ('Пам парам')