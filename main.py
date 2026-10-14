print("Поиск по каталогу. Команды: help. Выход: exit.")

while True:
    command = input("search> ")

    if command == "exit":
        break

    if command == "help":
        print("""
Доступные команды:
load <файл>
show
fields
filter add <поле> <оператор> <значение>
filter list
filter remove <номер>
filter clear
threshold <число>
search "<запрос>"
save <файл>
rate <id> <1..5>
ratings
exit
""")
if command == "load":
    print("Загрузка файла")
