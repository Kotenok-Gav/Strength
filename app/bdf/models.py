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
    

    
            


    def __str__(self):
        #Отображение названия модели
        return f"{self.text[:50]}"

