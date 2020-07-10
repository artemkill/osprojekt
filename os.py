import configparser
import os
import wget
clear = lambda: os.system("cls")
config = configparser.ConfigParser()
config.read("sysconf.ini")
fix0 = "\\"
print ("питон os версия ", (config["Confing"]["version"]), " используйте help для помощи по os.", sep='')
path = os.path.abspath('')
runprog = int(input("1 - run, 2 - exit: "))
if runprog == 1:
    while True:
        command = input("$ ")
        if command == "md":
            import ossoft
            name = input("dirname: ")
            try:
                os.mkdir(path+"\\documents\\"+name)
            except OSError:
                print (OSError, name)
            else:
                print ("Успешно создана директория %s " % name)
    
        elif command == "mkfile":
            name = input("name: ")
            print ("████████████████████████████████████████████████████████")
            print ("█████████████████████модификаторы███████████████████████")
            print ("████████████████████████████████████████████████████████")
            print ("█ w - создаёт/записывает в файл если он сущ то очищает █")
            print ("████████████████████████████████████████████████████████")
            print ("█ r - чтение файла                                     █")
            print ("████████████████████████████████████████████████████████")
            print ("█ a - дозапись                                         █")
            print ("████████████████████████████████████████████████████████")
            read = input("modif: ")
            try:
                filename = open(path+"\\documents\\"+f'{name}.txt', read)
                if read == "w":
                    print("\\n это enter, а stopwrite остановка редактирования и писать что угодно.")
                    while True:
                        writef = input()
                        if writef == "stopwrite":
                            break
                        elif writef == "\\n":
                            filename.write("\n")
                        else:
                            filename.write(writef)
                elif read == "a":
                    print("\\n это enter, а stopwrite остановка редактирования и писать что угодно.")
                    while True:
                        writef = input()
                        if writef == "stopwrite":
                            break
                        elif writef == "\\n":
                            filename.write("\n")
                        else:
                            filename.write(writef)
                elif read == "r":
                    filein = filename.read()
                    print(f"содержимое файла {name}\n{filein}")
            except ValueError:
                print (f"файл {filename} не удалось создать, файл существует или аргумент указан неверно")
            else:
                print("файл успешно создан/прочитан/записан")
                filename.close()
    
        elif command == "exit":
            exi = input("exit? Y/n: ")
            if exi == "y":
                break
            elif exi == "n":
                print ("не выходим")
            else:
                print ("неверный аргумент")
        elif command == "":
            pass
        elif command == "cls":
            clear()
            print ("питон os версия ", (config["Confing"]["version"]), " используйте help для помощи по os.", sep="")

        elif command == "path":
            print (path)
        
        elif command == "help":
            print ("помощь по питон os\nmd - создать директорию, mkfile - создать файл, exit - выйти, path - узнать путь к директории, cls - очистить экран, runprog - запустить программу. Всё! Новые команды ждите в обновлении.")
        elif command == "":
            pass
        elif command == "runprog":
            os.chdir(path)
            progname = input("progname: ")
            try:
                exec (f"import {progname}")
            except ModuleNotFoundError:
                print ("программа не существует")
            else:
                exec (f"{progname}.main()")
                os.chdir("..")
        else:
            print (f"неверная команда {command}")
elif runprog == 2:
    pass
