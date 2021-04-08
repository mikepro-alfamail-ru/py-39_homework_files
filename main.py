def is_int(string):
    try:
        result = int(string)
        return True
    except ValueError:
        return False

#Задание 1, вариант 1
def file_to_cookdict_readline(file):
    '''file - строка. Эта функция читает файл построчно.
    Окончание чтения проверяется по пустой строке'''
    cook_dict = {}
    with open(file, 'rt', encoding='utf-8') as f:
        eof = False
        while not eof:
            dish = f.readline().strip()
            if dish != '':
                cook_dict[dish] = []
                n = int(f.readline())
                for i in range(n):
                    ingridient = f.readline().strip().split(' | ')
                    cook_dict[dish].append(
                        {
                            'ingredient_name': ingridient[0],
                            'quantity': int(ingridient[1]),
                            'measure': ingridient[2]
                        }
                    )
                a = f.readline().strip()
            else:
                eof = True
    return cook_dict

#Задание 1, вариант 2
def file_to_cookdict(file):
    '''Эта функция считывает файл целиком. В этом случае нет необходимости писать количество ингридиентов. Переход к
    следующему рецепту осуществляется по пустой строке.'''
    cook_dict = {}
    with open(file, 'rt', encoding='utf-8') as f:
        cook_book = f.readlines()
    for line in cook_book:
        if line.strip() != '':
            if '|' not in line.strip():
               if not is_int(line.strip()):
                   dish = line.strip()
                   cook_dict[dish] = []
            else:
                ingridient = line.strip().split(' | ')
                cook_dict[dish].append(
                    {
                        'ingredient_name': ingridient[0],
                        'quantity': int(ingridient[1]),
                        'measure': ingridient[2]
                    }
                )
    return cook_dict

def file_to_cookdict_opt(file):
    cook_dict = {}
    with open(file, 'r', encoding='utf8') as f:
        for line in f:
            cook_dict[line.strip()] = []
            count = int(f.readline())
            for _ in range(count):
                ingredient = f.readline().strip().split(' | ')
                cook_dict[line.strip()].append(
                    {
                        'ingredient_name': ingredient[0],
                        'quantity': int(ingredient[1]),
                        'measure': ingredient[2]
                    }
                )
            f.readline()
    return cook_dict

#Задание 2
def get_shop_list_by_dishes(dishes, person_count, cook_dict):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_dict[dish]:
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[ingredient['ingredient_name']] = \
                    {
                        'quantity': ingredient['quantity'] * person_count,
                        'measure': ingredient['measure']
                    }
    return shop_list

cook_dict = file_to_cookdict_readline('recipes.txt')

data = file_to_cookdict_opt('recipes.txt')

with open('recipes1.txt', 'w', encoding='utf8') as f:
    for dish, ingredients in data.items():
        f.write(dish)
        f.write('\n')
        f.write(str(len(ingredients)))
        f.write('\n')
        for ingredient in ingredients:
            f.write(
                ingredient['ingredient_name'] +
                ' | ' +
                str(ingredient['quantity']) +
                ' | ' +
                ingredient['measure'] + '\n'
            )

        f.write('\n')


#
# pprint.pprint(cook_dict)
# pprint.pprint(file_to_cookdict('recipes.txt'))
# pprint.pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2, cook_dict))
# pprint.pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2, file_to_cookdict('recipes.txt')))
