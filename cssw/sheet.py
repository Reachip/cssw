import tempfile

import xlrd
import requests
import xlutils


class CohenSpreadSheet:
    def __init__(self):
        self.tempfile = tempfile.NamedTemporaryFile()
        self.tempfile.write(self._get_cohen_spread_sheet)
        work_book = xlrd.open_workbook(self.tempfile.name)
        self.number_of_leaf = work_book.sheet_names()
        self.leaf = work_book.sheet_by_name("Feuil1")

    @property
    def _get_cohen_spread_sheet(self) -> bytes:
        cohen_spred_sheet_url = "http://g.cohen.free.fr/telecharge/Calories.xls"
        cohen_spred_sheet = requests.get(cohen_spred_sheet_url, stream=True)

        if cohen_spred_sheet.status_code != 200:
            raise Exception(
                f"Can't get the document located at : {cohen_spred_sheet_url}"
            )

        return cohen_spred_sheet.content

    def get_food_by_food_family(self, food_family) -> list:
        return [self.leaf.cell_value(food, 0) for food in range(*food_family.value)]

    def get_nutriment_by_food_family(self) -> list:
        nutriment_by_food = []

        for food_position in range(*food_family.value):
            nutriment_value = self.leaf.cell_value(food_position, nutriment.value)
            food_name = self.leaf.cell_value(food_position, 0)
            nutriment_by_food.append((food_name, nutriment_value))

        return nutriment_by_food
