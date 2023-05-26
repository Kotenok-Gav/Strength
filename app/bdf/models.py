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
    

    
            


    def __str__(self):
        #Отображение названия модели
        return f"{self.text[:50]}"

