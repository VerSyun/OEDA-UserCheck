import os
from colorama import Fore, Style

class UserCheck():
    def __init__(self):
        pass

    userFile = "/etc/passwd"

    def getUserCount(self):
        return len(open(self.userFile, 'r').readlines())
    
    def setUserCount(self, userCount):
        return userCount
    
    def getLastLine(self):
        return open(self.userFile, "r").readlines()[-1]
    
    def setLastLine(self, LastLine):
        return LastLine
    
    def throwAlert(self):
        print(Fore.RED + Style.BRIGHT + 'Файл был изменен.' + Style.RESET_ALL)
        print("Добавлен новый пользователь " 
              + self.getLastLine().split(":")[0] 
              + " имеющий ID " 
              + self.getLastLine().split(":")[2])
        confirm = str(input('Это были вы? [Y/N]: '))
        return confirm
    
    def confirmCreation(self, confirmLetter):
        if (confirmLetter.lower() == 'y'):
            print(Fore.GREEN 
                  + Style.BRIGHT 
                  + 'Подтверждено' 
                  + Style.RESET_ALL)
            return True
        elif (confirmLetter.lower() == 'n'):
            os.system(f'passwd -l {self.getLastLine().split(":")[0]}')
            print(Fore.RED 
                  + f'Пользователь {self.getLastLine().split(":")[0]} заблокирован.' 
                  + Style.RESET_ALL)
            return False


if (__name__ == "__main__"):
    checker = UserCheck()
    checkerLastLine = checker.getLastLine()
    checkerUserCount = checker.getUserCount()
    while True:
        runLastLine = checker.getLastLine()
        runUserCount = checker.getUserCount()
        if (runUserCount > checkerUserCount):
            confirm = checker.throwAlert()
            result = checker.confirmCreation(confirm)
        checkerLastLine = checker.setLastLine(runLastLine)
        checkerUserCount = checker.setUserCount(runUserCount)