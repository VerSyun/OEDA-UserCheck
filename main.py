import os
import hashlib
from colorama import Fore, Style

file = '/etc/passwd'
startCheckSum = hashlib.md5(open(file, "rb").read()).hexdigest() #изначальная хеш-сумма, по которой определяется измененение файла
startFileSize = os.path.getsize(file) #размер нужен для того, чтобы понять, что конкретно было сделано
startLastLine = open(file, "r").readlines()[-1] #как правило, новый пользователь добавляется в конец файла, поэтому он нам понадобится

while True:
    runCheckSum = hashlib.md5(open(file, "rb").read()).hexdigest() #постоянный контроль хешсуммы
    runFileSize = os.path.getsize(file) #постоянный контроль размера
    runLastLine = open(file, "r").readlines()[-1] #постоянный контроль конца
    if (runCheckSum != startCheckSum): #замечено изменение
        print(Fore.RED + Style.BRIGHT + 'Файл был изменен.' + Style.RESET_ALL)
        if (runFileSize > startFileSize):
            print("Добавлен новый пользователь " + runLastLine.split(":")[0] + " имеющий ID " + runLastLine.split(":")[2])
        else:
            print("Удален пользователь " + startLastLine.split(":")[0] + " имеющий ID " + startLastLine.split(":")[2])
        confirm = str(input('Это были вы? [Y/N]: '))
        if (confirm.lower() == 'y'): #подтверждение изменения
            print(Fore.GREEN + Style.BRIGHT + 'Подтверждено' + Style.RESET_ALL)
            startCheckSum = runCheckSum
            startFileSize = runFileSize
            startLastLine = runLastLine
        elif (confirm.lower() == 'n'):
            #тут будет функционал отбирания прав
            break
        else:
            os.system('cls||clear') 
            print(Style.BRIGHT + Fore.CYAN +'НЕДОПУСТИМЫЙ ВВОД' + Style.RESET_ALL)
            
    del runCheckSum
    del runFileSize
    del runLastLine