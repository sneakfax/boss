from colorama import Fore, Back, Style
import os
import time


class UserInterface:

    def __init__(self ):
        pass

    def printWarning(self, msg):
        print(Fore.YELLOW+msg+Style.RESET_ALL)

    def printError(self, msg):
        print(Fore.RED+msg+Style.RESET_ALL)

    def logo(self):
            l = Fore.RED
            r = Fore.LIGHTRED_EX
            turbo ='888888b.    .d88888b.   .d8888b.   .d8888b.  \n'+\
                   '888  "88b  d88P" "Y88b d88P  Y88b d88P  Y88b \n'+\
                   '888  "88b  d88P" "Y88b d88P  Y88b d88P  Y88b \n'+\
                   '8888888K.  888     888  "Y888b.    "Y888b.   \n'+\
                   '888  "Y88b 888     888     "Y88b.     "Y88b. \n'+\
                   '888    888 888     888       "888       "888 \n'+\
                   '888   d88P Y88b. .d88P Y88b  d88P Y88b  d88P \n'+\
                   '8888888P"   "Y88888P"   "Y8888P"   "Y8888P"  \n'
                 
            spymer=l+"  ____    ____       _      __  __   __  __   _____   ____  \n"+\
                   l+" / ___|  |  _ \     / \    |  \/  | |  \/  | | ____| |  _ \ \n"+\
                   l+" \___ \  | |_) |   / _ \   | |\/| | | |\/| | |  _|   | |_) |\n"+\
                   l+"  ___) | |  __/   / ___ \  | |  | | | |  | | | |___  |  _ < \n"+\
                   l+" |____/  |_|     /_/   \_\ |_|  |_| |_|  |_| |_____| |_| \_\\n"
            logo=turbo+spymer+Style.RESET_ALL
            print(logo)

    def clear(self):
            os.system('cls' if os.name=='nt' else 'clear')

    def getUserIntegerInput(self, question):
        print(question)
        try:
            iterationsNumber = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
            int(iterationsNumber)
            return iterationsNumber
        except:
            self.printError("Разрешены только цифры!")
            self.getUserIntegerInput(question)



    def getUserChoice(self, question, options):
        availibleAnswer = []
        for i in range(len(options)):
            availibleAnswer.append(i+1)

        for x in range(len(options)):
            print(str(availibleAnswer[x])+". "+options[x]) 

        choice=-1
        while choice not in availibleAnswer:
            userInput=input(Fore.BLUE+question+Style.RESET_ALL+"~/")
            try:
                choice=int(userInput)
                if choice not in availibleAnswer:
                    self.printError("Неверный выбор, попробуйте еще раз! (Чтобы выйти нажмите CTRL-Z)")
            except:
                self.printError("Неверный выбор, попробуйте еще раз! (Чтобы выйти нажмите CTRL-Z)")

        return choice
