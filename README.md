
#Для Windows
#Открываем терминал
git clone https://github.com/Kotenok-Gav/Strength.git                 #Клонируем проект
python -m venv venv                                                   #Создаем папку виртуального окружения
venv/Scripts/activate                                                 #Активируем вирт. окружение
pip install —upgrade pip                                              #Обновляем менеджер пакетов
pip install -r requirements.txt                                       #Устанавливаем библиотеки
Скорее всего будут ошибки, сами устанавливаем:
pip install Django
pip install djangorestframework
pip install django-cors-headers
cd .\app\                                                            #Переходим в директорию Back-end
python manage.py migrate                                             #Создаем БД
python manage.py runserver                                           #Запускаем  Back-end

#Параллельно запускаем второй терминал
cd .\frontend\                                                       #Переходим в директорию Frontend
npm install                                                          #Устанавливаем зависимости
npm start                                                            #Запускаем Frontend
--------------------------------------------------------------

#Для Linux
#Открываем терминал
git clone https://github.com/Kotenok-Gav/Strength.git                 #Клонируем проект
python3.11 -m venv venv                                               #Создаем папку виртуального окружения
source venv/bin/activate                                              #Активируем вирт. окружение
pip install —upgrade pip                                              #Обновляем менеджер пакетов
pip install -r requirements.txt                                       #Устанавливаем библиотеки
Скорее всего будут ошибки, сами устанавливаем:
pip install Django
pip install djangorestframework
pip install django-cors-headers
cd ./app                                                             #Переходим в директорию Back-end
python manage.py migrate                                             #Создаем БД
python manage.py runserver                                           #Запускаем  Back-end

#Параллельно запускаем второй терминал
cd ./frontend                                                        #Переходим в директорию Frontend
npm install                                                          #Устанавливаем зависимости
npm start                                                            #Запускаем Frontend