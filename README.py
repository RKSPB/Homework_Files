from pprint import pprint
with open("menu.txt", "r", encoding="utf8") as text:
    cook_book = {}
    for line in text:
        dish = line.strip()
        ingredients_num = int(text.readline())
        formula = []
        for f in range(ingredients_num):
            ingredients, quantity, units = text.readline().strip().split(' | ')
            formula.append({
                'ingredient_name': ingredients,
                'quantity': quantity,
                'measure': units                                  
            })        
        text.readline()
        cook_book[dish] = formula
    pprint(cook_book, sort_dicts=False)
    print()
    

def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dict = {}
    for a, b in cook_book.items():
        if a in dishes:
            number_of_ingredients = {}           
            for c in b[:]:                                
                ingredient_name = c.get('ingredient_name') 
                ingredients_dict[ingredient_name] = {'measure' : c.get('measure'), 'quantity' : (int(c.get('quantity')) * person_count)}
    pprint(ingredients_dict)           
   
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)