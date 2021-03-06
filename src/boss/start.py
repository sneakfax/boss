#!/usr/bin/python3
import urllib3
import sys
import time
import threading
from threading import Thread
import subprocess
# from boss.sms import SmsSpammer
from boss.userInterface import UserInterface
from colorama import Fore, Back, Style
import os



#//////////////     TODO      ////////////////
def checkver():
    global ui
    # result = subprocess.check_output(["git", "diff"]).decode("utf-8") 
    result = ""
    if result != "":
        ui.printError("\nВерсия устарела и нуждается в обновлении!")
#//////////////     TODO      ////////////////


def update():
    global ui
    print("Вы уверены, что хотите обновить?")
    menuInput = ui.getUserChoice("spymer > ", ["Да","Нет"])
    if menuInput==1:
        os.system("cd && rm -rf spymer && git clone https://github.com/s0563858/spymer && cd spymer && python3 setup.py install")
        ui.printWarning("Успех! Теперь перезапустите программу!")
        exit()
    else:
        return "Отменено"

def oneNumber():
    global proxyManager
    global ui
    ui.clear()
    ui.logo()
    phone = ui.getUserIntegerInput('Введите телефон ("ctrl-Z" - выход):')
    iterationsNumber = ui.getUserIntegerInput('Введите количество кругов ("ctrl-Z" - выход):', limit=50)
    
    ui.clear()
    ui.logo()
    print('\nТелефон: {}\nКол-во кругов: {}'.format(phone,iterationsNumber)+'\nСпамер запущен.\nЕсли хотите остановить - нажмите Ctrl+Z.')
    doSpamming(phone, int(iterationsNumber))
    return Fore.GREEN+"\nГотово.\nТелефон: {}\nКол-во кругов: {}".format(phone, iterationsNumber)+Style.RESET_ALL




def severalNumbers():
    global ui
    ui.clear()
    ui.logo()
    #-------- Get phone numbers ----------
    print("Вы хотите использовать файл с номерами?")
    menuInput = ui.getUserChoice("spymer > ", ["Да","Нет"])
    phoneNumbers=[]
    if menuInput == 1:
        print("Введите путь к файлу: ")
        print("(Папка с файлом должна находиться в домашней дирректории!)")
        f_name=input(Fore.BLUE+"spymer > "+Style.RESET_ALL+"~/")
        try:
            os.chdir(os.getenv("HOME"))
            file=open("{}".format(f_name))
            phoneNumbers=file.read().splitlines()
            if phoneNumbers[-1] == '':
                    phoneNumbers.pop()
            print("Файл найден.\nНомера:\n{}".format(phoneNumbers))
        except FileNotFoundError:
            return Fore.RED+"\nФайл {} не найден".format(f_name)+Style.RESET_ALL
    else:
        print("Вводите номера: ")
        print("Чтобы закончить ввод номеров 'Enter'")
        newNumber="a"
        while newNumber != "":
            newNumber=input(Fore.BLUE+"spymer > "+Style.RESET_ALL+"~/")
            phoneNumbers.append(newNumber)
        phoneNumbers.pop()
        print("\nНомера:\n{}".format(phoneNumbers))
    #check if the numbers are correct:
    for phone in phoneNumbers:
        try:
            int(phone)
        except:
            return Fore.RED+"\nОдин из номеров состоит не только из цифр!"+Style.RESET_ALL
    #-------- Get phone numbers ----------

    ui.clear()
    ui.logo()
    iterationsNumber = ui.getUserIntegerInput('Введите количество кругов ("ctrl-Z" - выход):',limit=50)

    ui.clear()
    ui.logo()
    print('\nКол-во кругов: {}'.format(iterationsNumber))
    thread_list = []
    for phone in phoneNumbers:
        print('\nЗапущен спам на {}.Если хочешь остановить - нажмите Ctrl+Z.'.format(phone))
        t = threading.Thread (target=doSpamming, args=(phone,iterationsNumber))
        thread_list.append(t)
        t.start()
    #wait for all threads to finish:
    for x in thread_list:
        x.join()
    return Fore.GREEN+"\nГотово.\nНомера:{}\nКол-во кругов: {}".format(phoneNumbers,iterationsNumber)+Style.RESET_ALL


def doSpamming(phone, iterationsNumber):
    global proxyManager
    iteration=0
    spammer = SmsSpammer(phone)
    while iteration < iterationsNumber:
        proxies = proxyManager.getProxies()
        spammer.setProxies(proxies)
        print(Fore.LIGHTBLUE_EX+"Круг "+str(iteration)+" начат..."+Style.RESET_ALL)
        spammer.startSending()
        iteration+=1
        print(Fore.GREEN+"{}".format(phone)+Style.RESET_ALL+": круг №{} пройден.".format(iteration))
        if spammer.timeoutCounter > 10:
            print(Fore.RED+"\nМногие сообщения не были отосланы - возмножна проблема с интернет-соеденением или проблема с прокси!"+Style.RESET_ALL)
    print(Fore.GREEN+"\nСпам на {} закончен. Кол-во кругов {}".format(phone, iterationsNumber)+Style.RESET_ALL)

def startApplication():
    global proxyManager
    global ui
    ui = UserInterface()
    proxyManager = ProxyManager()
    proxyManager.autoChangeProxy = True
    
    result=""
    while True:
        ui.clear()
        ui.logo()
        checkver()
        print(result)

        #------proxy-status------
        if proxyManager.proxyList == [] and not proxyManager.autoChangeProxy:
            ui.printWarning("Советую использовать прокси !!!")
            print("Proxy: "+Fore.BLUE+"no proxy"+Style.RESET_ALL)
        else: 
            if proxyManager.autoChangeProxy:
                print("Proxy: "+Fore.BLUE+"auto-change"+Style.RESET_ALL)
            else:
                print("Proxy: "+Fore.BLUE+"{}".format(proxyManager.proxyList)+Style.RESET_ALL)
        #------proxy-status------


        menuInput = ui.getUserChoice("Введите номер пункта: ", ["Запустить спамер","Настройки прокси","Обновить SPYMER","Выход"])
        if menuInput == 1:
            ui.clear()
            ui.logo()
            menuInput = ui.getUserChoice("Выберите один вариант: ", ["Запустить спамер на один номер","Запустить спамер на несколько номеров"])
            if menuInput == 1:
                result=oneNumber()
            elif menuInput == 2:
                result=severalNumbers()
        elif menuInput == 2:
            autoChangeStatus = "Отключить"
            if not proxyManager.autoChangeProxy:
                autoChangeStatus = "Включить"
            menuInput = ui.getUserChoice("spymer >  ", ["Удалить прокси","Ввести свой прокси","Сгенерировать прокси",autoChangeStatus+" автоматическую генерацию прокси после каждого круга"])
            ui.clear()
            ui.logo()
            if menuInput==1:
                proxyManager.proxyList = []
                proxyManager.autoChangeProxy = False
            elif menuInput==2:
                proxyManager.updateproxy()
            elif menuInput==3:
                proxyManager.generateproxy()
            elif menuInput==4:
                proxyManager.autoChangeProxy = not proxyManager.autoChangeProxy 

        elif menuInput == 3:
            ui.clear()
            ui.logo()
            result=update()
        
        elif menuInput == 4:
            print (Fore.BLUE+"\nДо скорой встречи!)\n"+Style.RESET_ALL)
            exit()




#async version for pc:
def asyncMain():
    global SmsSpammer
    global ProxyManager
    from boss.asyncRequestSender.proxyManager import ProxyManager
    from boss.asyncRequestSender.sms import SmsSpammer
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    startApplication()
#mobile version:
def main():
    global SmsSpammer
    global ProxyManager
    from boss.requestSender.sms import SmsSpammer
    from boss.requestSender.proxyManager import ProxyManager
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    startApplication()


