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

    # 2.1.2 Эквивалентная толщина стенки ракеты   м, с точностью до тысячных
    tol_R = models.DecimalField(decimal_places=3, max_digits=4)

    # 2.1.3 Длина ракеты:  м, с точностью до десятых
    L = models.DecimalField(decimal_places=1, max_digits=4)

    
    # 2.2.1 Диаметр контейнера:  м, с точностью до сотых
    d0_Kon = models.DecimalField(decimal_places=2, max_digits=3)

    
    # 2.2.2 Эквивалентная толщина стенки контейнера   м, с точностью до тысячных
    tol_Kon = models.DecimalField(decimal_places=3, max_digits=4)

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


    #------------------------------------------------------------------------

    # 4 Граничные и начальные условия
    # 4.1 Скорость бокового набегающего потока:  м/с
    V_sredy = models.DecimalField(decimal_places=1, max_digits=5)

    # 4.2 Задание тяги двигателя (Н) в зависимости от времени (с)

    t_p1 = models.DecimalField(decimal_places=2, max_digits=6)
    P1 = models.IntegerField()

    t_p2 = models.DecimalField(decimal_places=2, max_digits=6)
    P2 = models.IntegerField()

    t_p3 = models.DecimalField(decimal_places=2, max_digits=6, null = True, blank=True)
    P3 = models.IntegerField(null = True, blank=True)

    t_p4 = models.DecimalField(decimal_places=2, max_digits=6, null = True, blank=True)
    P4 = models.IntegerField(null = True, blank=True)

    t_p5 = models.DecimalField(decimal_places=2, max_digits=6, null = True, blank=True)
    P5 = models.IntegerField(null = True, blank=True)

    t_p6 = models.DecimalField(decimal_places=2, max_digits=6, null = True, blank=True)
    P6 = models.IntegerField(null = True, blank=True)

    t_p7 = models.DecimalField(decimal_places=2, max_digits=6, null = True, blank=True)
    P7 = models.IntegerField(null = True, blank=True)

    t_p8 = models.DecimalField(decimal_places=2, max_digits=6, null = True, blank=True)
    P8 = models.IntegerField(null = True, blank=True)

    t_p9 = models.DecimalField(decimal_places=2, max_digits=6, null = True, blank=True)
    P9 = models.IntegerField(null = True, blank=True)

    t_p10 = models.DecimalField(decimal_places=2, max_digits=6, null = True, blank=True)
    P10 = models.IntegerField(null = True, blank=True)

    t_p11 = models.DecimalField(decimal_places=2, max_digits=6, null = True, blank=True)
    P11 = models.IntegerField(null = True, blank=True)

    t_p12 = models.DecimalField(decimal_places=2, max_digits=6, null = True, blank=True)
    P12 = models.IntegerField(null = True, blank=True)

    t_p13 = models.DecimalField(decimal_places=2, max_digits=6, null = True, blank=True)
    P13 = models.IntegerField(null = True, blank=True)
    

    #------------------------------------------------------------------------

    # 5 Распределение масс конструкции
    # 5.1 Стартовая масса ракеты:  кг, с точностью до десятых
    m = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.2 Масса ГЧ:  кг
    m_gch = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.3 Расстояние от нижнего края ракеты до точки приложения массы ГЧ:  м, с точностью до десятых
    X_gch = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.4 Масса СУ ракеты:  кг
    m_cy = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.5 Расстояние от нижнего края ракеты до точки приложения массы СУ:  м, с точностью до десятых
    X_cy = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.6 Масса ДУ 1 ступени:  кг
    m_dy_1 = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.7 Расстояние от нижнего края ракеты до точки приложения массы ДУ 1 ступени:  м, с точностью до десятых
    X_dy_1 = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.8 Масса окислителя 1 ступени:  кг
    mo_1 = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.9 Длина бака окислителя 1 ступени:  м, с точностью до десятых
    Lo_1 = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.10 Расстояние от нижнего края ракеты до нижнего днища бака окислителя 1 ступени:  м, с точностью до десятых
    Xo_1 = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.11 Масса горючего 1 ступени:  кг
    mg_1 = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.12 Длина бака горючего 1 ступени:  м, с точностью до десятых
    Lg_1 = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.13 Расстояние от нижнего края ракеты до нижнего днища бака горючего 1 ступени:  м, с точностью до десятых
    Xg_1 = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.14_1 Расстояние от нижнего края контейнера до первой точки крепления (0.0) в м
    L_kon_zakr_1 = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.14_2 Тип закрепления
    tip_zakr_1 = models.PositiveSmallIntegerField()

    # 5.15_1 Расстояние от нижнего края контейнера до второй точки крепления (2.8) в м
    L_kon_zakr_2 = models.DecimalField(decimal_places=1, max_digits=12)

    # 5.15_2 Тип закрепления
    tip_zakr_2 = models.PositiveSmallIntegerField()

    # 5.16_1 Расстояние от нижнего края контейнера до третьей точки крепления (6.3) в м
    L_kon_zakr_3 = models.DecimalField(decimal_places=1, max_digits=12, null = True, blank=True)

    # 5.16_2 Тип закрепления
    tip_zakr_3 = models.PositiveSmallIntegerField(null = True, blank=True)

    # 5.17_1 Расстояние от нижнего края контейнера до четвертой точки крепления (9.1) в м
    L_kon_zakr_4 = models.DecimalField(decimal_places=1, max_digits=12, null = True, blank=True)

    # 5.17_2 Тип закрепления
    tip_zakr_4 = models.PositiveSmallIntegerField(null = True, blank=True)

    # 5.18_1 Расстояние от нижнего края контейнера до пятой точки крепления (13.5) в м
    L_kon_zakr_5 = models.DecimalField(decimal_places=1, max_digits=12, null = True, blank=True)

    # 5.18_2 Тип закрепления
    tip_zakr_5 = models.PositiveSmallIntegerField(null = True, blank=True)


    #------------------------------------------------------------------------

    # 6 Свойства конструкционных материалов
    # 6.1 Ракета
    # 6.1.1 Модуль Юнга (упругости): МПа, с точностью до десятых
    modul_unga1 = models.DecimalField(decimal_places=1, max_digits=12)

    # 6.1.2 Коэффициент Пуассона:  с точностью до сотых
    koeff_puass1 = models.DecimalField(decimal_places=2, max_digits=6)

    # 6.2 Контейнер
    # 6.2.1 Модуль Юнга (упругости): МПа, с точностью до десятых
    modul_unga2 = models.DecimalField(decimal_places=1, max_digits=12)

    # 6.2.2 Коэффициент Пуассона:  с точностью до сотых
    koeff_puass2 = models.DecimalField(decimal_places=2, max_digits=6)

    # 6.2.3 Плотность:  ,кг/м3 точностью до целых
    plotnost2 = models.IntegerField()

    
    

    
            


    def __str__(self):
        #Отображение названия модели
        return f"{self.text[:50]}"

