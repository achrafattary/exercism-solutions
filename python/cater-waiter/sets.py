from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name,set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    for e in drink_ingredients:
        if e in ALCOHOLS :
            return ' '.join([drink_name,"Cocktail"])
    return ' '.join([drink_name,"Mocktail"])



def categorize_dish(dish_name, dish_ingredients):
    if dish_ingredients.issubset(VEGAN):
        return ": ".join([dish_name,'VEGAN'])
    elif dish_ingredients.issubset(VEGETARIAN):
        return ": ".join([dish_name,'VEGETARIAN'])
    elif dish_ingredients.issubset(PALEO):
        return ": ".join([dish_name,'PALEO'])
    elif dish_ingredients.issubset(KETO):
        return ": ".join([dish_name,'KETO'])
    else :
        return ": ".join([dish_name,'OMNIVORE'])

def tag_special_ingredients(dish):
    return (dish[0],set(dish[1]).intersection(SPECIAL_INGREDIENTS))



def compile_ingredients(dishes):
    master_list = set()
    for e in dishes:
        master_list = master_list.union(e)
    return master_list


def separate_appetizers(dishes, appetizers):
    dishes_set = set(dishes)
    appetizers_set = set(appetizers)

    return dishes_set.difference(appetizers_set)


def singleton_ingredients(dishes, intersection):
    singl = set()
    for e in dishes:
        dif = e.difference(intersection)
        print(dif)
        singl = singl.union(dif)
    return singl
