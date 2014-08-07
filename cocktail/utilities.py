import categories


def encode(string):
    return unicode(string.decode('utf-8'))


def is_type(string):
    matches = []
    if len(string) > 1:
        for type in categories.all_types:
            if string in type:
                matches.append(type)
        if len(matches) > 0:
            return True, min(matches, key=len)[0]
    return False, string


def split_on_types(ingredients):
    type_ingredients = set()
    name_ingredients = set()

    for ingredient in ingredients:
        was_type, search_term = is_type(ingredient)
        if was_type:
            type_ingredients.add(search_term)
        else:
            name_ingredients.add(ingredient)

    return type_ingredients, name_ingredients

