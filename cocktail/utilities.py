import categories


def encode(string):
    return unicode(string.decode('utf-8'))


def is_type(string):
    for alcohol_type in categories.all_types:
        if string == alcohol_type:
            return True, alcohol_type
    return False, string


def is_substring_of_type(string):
    matches = []
    for alcohol_type in categories.all_types:
        if string in alcohol_type:
            matches.append(alcohol_type)
    if len(matches) > 0:
        matches.sort(key=len)
        return True, matches
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

