
def cooking():
    with open('list.txt', encoding='utf-8') as file_object:
        cook_book = {}
        for line in file_object:
            line = line.strip()
            cook_book.update({line: []})
            name = int(file_object.readline().strip())
            for r in range(name):
                list_1 = file_object.readline().strip().split(' | ')
                dict_1 = {'ingredient_name': list_1[0],
                          'quantity': int(list_1[1]),
                          'measure': list_1[2]}
                cook_book[line].append(dict_1)
            file_object.readline()
    return cook_book


print(cooking())
print('----------------------------------------------------')


def get_shop_list_by_dishes(dishes, person_count):
    try:
        shopping_list = {}
        for dish in dishes:
            for ingredient in cooking()[dish]:
                name_dish = dict(ingredient)
                name_dish['quantity'] *= person_count

                if name_dish['ingredient_name'] not in shopping_list:
                    shopping_list[name_dish['ingredient_name']] = name_dish
                    del name_dish['ingredient_name']

                # my_1 = {k: v for k, v in name_dish.items() if k != 'ingredient_name'}




        return shopping_list


    except KeyError:
        print('Error')


print(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 1))


