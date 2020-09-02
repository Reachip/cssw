from cssw.food import Food
from cssw.nutriment import Nutriment

import xlrd
from urllib import request

class CohenSpreadSheet:
    def __init__(self):
        work_book = xlrd.open_workbook(self._get_cohen_spread_sheet)
        self.number_of_leaf = work_book.sheet_names()
        self.leaf = work_book.sheet_by_name("Feuil1")

    @property
    def _get_cohen_spread_sheet(self) -> bytes:
        cohen_spred_sheet_url = "http://g.cohen.free.fr/telecharge/Calories.xls"

        try:
            file_location, header = request.urlretrieve(cohen_spred_sheet_url)
            return file_location

        except Exception as why:
            print(f"Can't get the document located at {cohen_spred_sheet_url} : {why}")        

    def get_food_by_food_family(self, food_family: Food) -> list:
        return [self.leaf.cell_value(food, 0) for food in range(*food_family.value)]

    def get_nutriment_by_food_family(self, nutriment: Nutriment, food_family: Food) -> list:
        nutriment_by_food = []

        for food_position in range(*food_family.value):
            nutriment_value = self.leaf.cell_value(food_position, nutriment.value)
            food_name = self.leaf.cell_value(food_position, 0)
            nutriment_by_food.append((food_name, nutriment_value))

        return nutriment_by_food
