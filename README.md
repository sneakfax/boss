[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0) ![repo-size](https://img.shields.io/github/repo-size/sneakfax/boss)


![N|Solid](https://i.ibb.co/c1XFvLC/bosss4.jpg)
#
#### SMS-спамер который спамит СМС-подтверждениями с разных сайтов.<br>
#### Только для России!<br>


# Функции:
Данный спамер содержит следуйщие функции:
1. Спам СМС-подтверждениями с 16 разных сервисов
2. Возможность установить количество спам-рассылок (= сколько раз должны быть отосланы СМС-подтверждения)
3. Спам сразу на несколько номеров
4. Спам через прокси (чтобы скрыть IP и избежать блокировки при спаме)
5. Спам через один прокси или сразу через несколько
6. *Асинхронность* - рассылка спама производится очень быстро (= программа пытается отослать смс сразу через несколько сервисов и не ждет пока отсылка через один сервис будет успешной)
7. Функция автоматической смены прокси после каждой спам рассылки
8. Возможность просто добавлять новые сервисы (в файле <code>servicesList.json</code>)

# Как установить?
   Просто следуйте одной из инструкций<br>
## Android:
   Если у вас Android - скачать <a href="https://play.google.com/store/apps/details?id=com.termux&hl=ru">Termux из Google Play</a>, открыть его и прописать команды ниже:<br>
    <code>apt update</code><br>
    <code>apt upgrade</code><br>
    <code>apt install git</code><br>
     <code>apt install python</code><br>
    <code>git clone https://github.com/sneakfax/boss</code><br>
    <code>cd boss</code><br>
    <code>python3 setup_mobile.py install</code><br>
    <code>boss</code><br>

## iOS:
   Если у вас iOS - скачать <a href="https://apps.apple.com/ru/app/testflight/id899247664">Testflight из App Store</a>, после чего присоедениться к тестированию <a href="https://testflight.apple.com/join/97i7KM8O">iSH в Testflight</a> и прописать команды ниже:<br>
    <code>apk update</code><br>
    <code>apk upgrade</code><br>
    <code>apk add git python3 py3-pip</code><br>
    <code>git clone https://github.com/sneakfax/boss</code><br>
    <code>cd boss</code><br>
    <code>python3 setup_mobile.py install</code><br>
    <code>boss</code><br>
    <br>

## Windows:
   С начала установите Windows WSL - как это делается можно посмотреть <a href="https://www.youtube.com/watch?v=HYuFw-YldjU">здесь</a>.
    После установки Ubuntu WSL - запустите Ubuntu WSL и пробейте следуйщие комманды:<br>
    <code>sudo add-apt-repository universe</code><br>
    <code>sudo apt-get update</code><br>
    <code>sudo apt install git</code><br>
    <code>git clone https://github.com/sneakfax/boss</code><br>
    <code>cd boss</code><br>
    <code>python3 setup.py install</code><br>
    <code>boss</code><br>

## Linux:
   Установка на Linux аналогична установке на Windows (только без устоновки Ubuntu WSL), нужно лишь вбить команды в терминале.<br>

## MacOS:
   Сначала установите brew если он у вас еще не установлен. Откройте терминал и вбейте:<br>
    <code>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</code><br>
    После этого пропишите в терминале следуйщие комманды:<br>
    <code>brew upgrade --cask</code><br>
    <code>brew install python3</code><br>
    <code>brew install git</code><br>
    <code>git clone https://github.com/sneakfax/boss</code><br>
    <code>cd boss</code><br>
    <code>python3 setup.py install</code><br>
    <code>boss</code><br>




# LICENSE
   **Лицензия: MPL-2.0**<br>
   Если вы пользуетесь данной программой вы соглашаетесь с лицензией MPL-2.0.<br>
   **Согласно MPL-2.0 разработчики не несут ответственности за действия которые делались с помощью данной программы** (т.е. если у вас будут проблемы с законом - эти проблемы остаются у вас). 
   
   Это шуточная программа: пожалуйста не используйте ее на незнакомых вам людях или с целью навредить кому-либо. 
