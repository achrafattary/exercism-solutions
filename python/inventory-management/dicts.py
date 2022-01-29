def create_inventory(items):
    dictionary = {}
    for e in set(items):
        dictionary[e] = items.count(e)
    return dictionary


def add_items(inventory, items):
    dic = create_inventory(items)
    x = list(inventory.items())
    for e in x :
        if e[0] in dic :
            dic[e[0]] = dic[e[0]] + e[1]
        else:
            dic[e[0]] = e[1]
    return dic


def decrement_items(inventory, items):
    for e in items:
        if (inventory[e] >= 1):
            inventory[e] -= 1
    return inventory


def remove_item(inventory, item):
    try :
        inventory.pop(item)
        return inventory
    except IndexError:
        print('item not in inventory')
    finally :
        return inventory
    

def list_inventory(inventory):
    lst = list(inventory.items())
    for item in lst:
        if item[1] == 0:
            lst.remove(item)
    return lst