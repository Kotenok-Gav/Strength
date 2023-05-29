from django.db import models
from django.contrib.auth.models import User

class Rockets_bdf(models.Model):
    #help_text="текст подсказка около поля"
    #verbose_name='Напишите что нибудь'

    # 1_Общие данные
    # 1.1.1 Название проекта
    text = models.CharField(max_length=200)

    # 1.1.2 Время создания
    data_added = models.DateTimeField(auto_now_add=True, null=True)   

    # 1.2 Определение старта ракеты
    start_rocket = models.PositiveSmallIntegerField()

    # 1.3 Время выхода ракеты из контейнера в секундах с точностью до тысячных
    t = models.DecimalField(decimal_places=3, max_digits=6)

    #------------------------------------------------------------------------

    # 2 Геометрические характеристики
    # 2.1.1 Диаметр ракеты:  м, с точностью до сотых
    d0 = models.DecimalField(decimal_places=2, max_digits=3)

    #(НЕТ)
    # 2.1.2 Эквивалентная толщина стенки ракеты   м, с точностью до тысячных
    tol_R = models.DecimalField(decimal_places=3, max_digits=4)

    # 2.1.3 Длина ракеты:  м, с точностью до десятых
    L = models.DecimalField(decimal_places=1, max_digits=4)

    #(НЕТ)
    # 2.2.1 Диаметр контейнера:  м, с точностью до сотых
    d0_Kon = models.DecimalField(decimal_places=2, max_digits=3)

    #(НЕТ)
    # 2.2.2 Эквивалентная толщина стенки контейнера   м, с точностью до тысячных
    tol_Kon = models.DecimalField(decimal_places=3, max_digits=4)

    #(НЕТ)
    # 2.2.3 Длина контейнера:  м, с точностью до десятых
    L_Kon = models.DecimalField(decimal_places=1, max_digits=4)

    #------------------------------------------------------------------------

    # 3 Параметры опорно-ведущих поясов (ОВП)
    # 3.1 Количество опорно-ведущих поясов (ОВП):  Введите число от 1 до 5
    kolichestvo_amort = models.PositiveSmallIntegerField() 

    # 3.2 Жесткость ОВП:  МН/м (с точностью до десятых)
    zhestkost_amort = models.DecimalField(decimal_places=1, max_digits=12)

    # 3.3.1 Введите расстояние: от нижнего края ракеты до верхнего (первого) пояса амортизации в м с точностью до десятых
    X1 = models.DecimalField(decimal_places=1, max_digits=6)

    # 3.3.2 Введите расстояние: от нижнего края ракеты до второго пояса амортизации в м с точностью до десятых
    X2 = models.DecimalField(decimal_places=1, max_digits=6, null = True, blank=True)

    # 3.3.3 Введите расстояние: от нижнего края ракеты до третьегопояса амортизации в м с точностью до десятых
    X3 = models.DecimalField(decimal_places=1, max_digits=6, null = True, blank=True)

    # 3.3.4 Введите расстояние: от нижнего края ракеты до четвертого пояса амортизации в м с точностью до десятых
    X4 = models.DecimalField(decimal_places=1, max_digits=6, null = True, blank=True)

    # 3.3.5 Введите расстояние: от нижнего края ракеты до пятого пояса амортизации в м с точностью до десятых
    X5 = models.DecimalField(decimal_places=1, max_digits=6, null = True, blank=True)
    
    

    
            


    def __str__(self):
        #Отображение названия модели
        return f"{self.text[:50]}"

