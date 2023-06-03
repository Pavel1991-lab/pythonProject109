import json
self_ing = ['limon', 'mint']


def find_coctail(self_ing):
    with open('coctail.json', 'r') as coctail:
        coc = json.load(coctail)
        if coc.get("ingredients") == self_ing:
            return coc.get("name")
    return None


def choose_ing():


    i = 0
    with open('coctail.json', 'r') as coctail:
        coc = json.load(coctail)
    for ing in  self_ing:
        i += 1
        print(f'{i} - {ing}')
    inga = []
    while True:

        command = input('Введитие')
        if command == '0':
            return inga
        else:
            if command.isdigit():
                num = int(command)
                if num > len(self_ing):
                    print('Такого нету')
                else:
                    inga.append(self_ing[num - 1])
            else:
                print('Нужен номер')

