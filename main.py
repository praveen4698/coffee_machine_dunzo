import unittest

from coffee_machine import CoffeeMachine
from ingredient_not_available_exception import IngredientNotAvailableException


class coffee_machine_handler:
    ingredient_quantity_mapping = {
      "hot_water": 500,
      "hot_milk": 500,
      "ginger_syrup": 100,
      "sugar_syrup": 100,
      "tea_leaves_syrup": 100,
      "green_mixture" : 100
    }

    drink_types = {
        "hot_tea" : {
            "hot_water": 200,
            "hot_milk": 100,
            "ginger_syrup": 10,
            "sugar_syrup": 10,
            "tea_leaves_syrup": 30
        },
        "hot_coffee" : {
            "hot_water": 100,
            "ginger_syrup": 30,
            "hot_milk": 400,
            "sugar_syrup": 50,
            "tea_leaves_syrup": 30
        },
        "black_tea" : {
            "hot_water": 300,
            "ginger_syrup": 30,
            "sugar_syrup": 50,
            "tea_leaves_syrup": 30
        },
        "green_tea" : {
            "hot_water": 100,
            "ginger_syrup": 30,
            "sugar_syrup": 50,
            "green_mixture": 30
        }
    }


    def __init__(self):
        self.__coffee_machine = CoffeeMachine(outlets=3, ingredients_dict=self.ingredient_quantity_mapping, drink_types=self.drink_types)

    def make_coffee(self, drink_type):
        return self.__coffee_machine.make_drink(drink_type=drink_type)

    def add_ingredients(self, ingredient_name , quantity):
        return self.__coffee_machine.add_quantity_ingredient(ingredient_name, quantity)


class coffee_machine_tests(unittest.TestCase):

    def test_case_1(self):
        print("Test case :  1")
        coffee_machine = coffee_machine_handler()
        self.assertEqual(coffee_machine.make_coffee('hot_tea'), "hot_tea is prepared")
        self.assertEqual(coffee_machine.make_coffee('hot_tea'), "hot_tea is prepared")
        self.assertIsInstance(coffee_machine.make_coffee('hot_tea'), IngredientNotAvailableException)

    def test_case_2(self):
        print("Test case :  2")
        coffee_machine = coffee_machine_handler()
        self.assertEqual(coffee_machine.make_coffee('green_tea'), "green_tea is prepared")
        self.assertEqual(coffee_machine.make_coffee('black_tea'), "black_tea is prepared")
        self.assertIsInstance(coffee_machine.make_coffee('hot_coffee'), IngredientNotAvailableException)

    def test_case_3(self):
        print("Test case :  3")
        coffee_machine = coffee_machine_handler()
        self.assertEqual(coffee_machine.make_coffee('green_tea'), "green_tea is prepared")
        self.assertEqual(coffee_machine.make_coffee('black_tea'), "black_tea is prepared")
        coffee_machine.add_ingredients('sugar_syrup', 250)
        self.assertEqual(coffee_machine.make_coffee('hot_coffee'), "hot_coffee is prepared")


if __name__ == '__main__':
    test_cases = coffee_machine_tests()
    test_cases.test_case_1()
    test_cases.test_case_2()
    test_cases.test_case_3()