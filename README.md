<h1 align="center">Hi there, I'm <a href="https://daniilshat.ru/" target="_blank">ILYA</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Lover of rockets and sweet horses from Chelyabinsk</h3>


[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Fullstack+web+developer)](https://git.io/typing-svg)



Инструкция для запуска проекта  
Для Windows  

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