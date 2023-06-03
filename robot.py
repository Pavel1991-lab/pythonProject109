import json


class Robot:
    def __init__(self):
        self.ing = ['limon', 'mint', 'soda']
        self.get_coct()


    def __call__(self, *args, **kwargs):
        while True:
            self.__help_text()
            command = input('Введитие команду')
            if command == '0':
                break
            if command == '1':
                a = self.choose_ing()
                print(self.find_coctail(a))

            else:
                print(f'Такой команды нету')

    def __help_text(self):
        print('Доступные команды')
        print('1- Выбрать ингридеент')
        print('0 - Выход')

    # def find_coctail(curr):
    #     with open('coctail.json', 'r') as coctail:
    #         coc = json.load(coctail)
    #     for c in coc:
    #         if coc.get("ingredients") == curr:
    #             return coc.get("name")
    #     return None

    def find_coctail(self, curr):
            coc = self.get_coct()
            if sorted(coc.get("ingredients")) == sorted(curr):
                return coc.get("name")

            return "что не то"

    def choose_ing(self):


        i = 0
        for ing in self.ing:
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
                    if num > len(self.ing):
                        print('Такого нету')
                    else:
                        inga.append(self.ing[num-1])
                else:
                    print('Нужен номер')


    def get_coct(self):
        with open("coctail.json",  'r') as f:
            self.coctails = json.load(f)
        return self.coctails





if __name__ == "__main__":
    robo = Robot()
    robo()


