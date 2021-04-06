import pprint

def is_int(string):
    try:
        result = int(string)
        return True
    except ValueError:
        return False

#Задание 1, вариант 1
def file_to_coockdict_readline(file):
    '''file - строка. Эта функция читает файл построчно.
    Окончание чтения проверяется по пустой строке'''
    coock_dict = {}
    with open(file, 'rt', encoding='utf-8') as f:
        eof = False
        while not eof:
            dish = f.readline().strip()
            if dish != '':
                coock_dict[dish] = []
                n = int(f.readline())
                for i in range(n):
                    ingridient = f.readline().strip().split(' | ')
                    coock_dict[dish].append({'ingredient_name': ingridient[0], 'quantity': int(ingridient[1]), 'measure': ingridient[2]})
                a = f.readline().strip()
            else:
                eof = True
    return coock_dict

#Задание 1, вариант 2
def file_to_coockdict(file):
    '''Эта функция считывает файл целиком. В этом случае нет необходимости писать количество ингридиентов. Переход к
    следующему рецепту осуществляется по пустой строке.'''
    coock_dict = {}
    with open(file, 'rt', encoding='utf-8') as f:
        coock_book = f.readlines()
    for line in coock_book:
        if line.strip() != '':
            if '|' not in line.strip():
               if not is_int(line.strip()):
                   dish = line.strip()
                   coock_dict[dish] = []
            else:
                ingridient = line.strip().split(' | ')
                coock_dict[dish].append({'ingredient_name': ingridient[0], 'quantity': int(ingridient[1]), 'measure': ingridient[2]})
    return coock_dict


#Задание 2
def get_shop_list_by_dishes(dishes, person_count, coock_dict):
    shop_list = {}
    for dish in dishes:
        for ingredient in coock_dict[dish]:
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
            else:
                shop_list[ingredient['ingredient_name']] = {'quantity': ingredient['quantity'], 'measure': ingredient['measure']}
    return shop_list

coock_dict = file_to_coockdict_readline('recipes.txt')

pprint.pprint(coock_dict)
pprint.pprint(file_to_coockdict('recipes.txt'))
pprint.pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2, coock_dict))
pprint.pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2, file_to_coockdict('recipes.txt')))
