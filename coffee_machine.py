import threading

from ingredient_not_available_exception import IngredientNotAvailableException


class CoffeeMachine:
    __outlets = None
    __ingredient_quantity_mapping = dict()
    __drinks_ingredients_mapping = dict()
    __lock = None
    def __init__(self, ingredients_dict, drink_types, outlets):

        self.__outlets = outlets
        self.__lock = threading.Lock()

        for ingredient, quantity in ingredients_dict.items():
            self.__ingredient_quantity_mapping.update({
                ingredient : quantity
            })

        for drink, ingredient in drink_types.items():
            self.__drinks_ingredients_mapping.update({
                drink :  ingredient
            })

    def add_quantity_ingredient(self, ingredient_name, quantity):
        self.__ingredient_quantity_mapping[ingredient_name] += quantity

    def get_quantity_ingredient(self, ingredient_name):
        return self.__ingredient_quantity_mapping.get(ingredient_name)

    def _get_ingredients(self, drink_type):

        threading.Lock()
        for drink_ingredient, quantity in self.__drinks_ingredients_mapping.get(drink_type).items():
            if not self.__ingredient_quantity_mapping.get(drink_ingredient) or self.__ingredient_quantity_mapping.get(drink_ingredient) < quantity:
                print("{} cannot be prepared because item {} is not sufficient".format(drink_type, drink_ingredient))
                raise IngredientNotAvailableException()

        required_ingredients = dict()
        for drink_ingredient, quantity in self.__drinks_ingredients_mapping.get(drink_type).items():
            self.__ingredient_quantity_mapping[drink_ingredient] -= quantity
            required_ingredients.update({
                drink_ingredient : quantity
            })

        return  required_ingredients

    def _get_drink(self, drink_type):
        return "{} is prepared".format(drink_type)

    def make_drink(self, drink_type):


        try:
            self.__lock.acquire()
            required_ingredients = self._get_ingredients(drink_type=drink_type)
        except IngredientNotAvailableException :
            return IngredientNotAvailableException()
        finally:
            self.__lock.release()

        drink = self._get_drink(drink_type=drink_type)
        print(drink)

        return drink


