# Cohen Spread Sheet Wrapper 

:fr:

"Wrapper" du tableau Excel du Docteur Jean-Michel Cohen référencent les différentes quantités de nutriments que contient un aliment classés par famille d'aliments.

:uk:

A wrapper to use the spread sheet of Dr. Jean-Michel Cohen concerning nutrition nutriments quantity per food family.

# Example :uk: | Exemple :fr:

```python
from cssw.sheet import CohenSpreadSheet
from cssw.food import CohenSpreadSheetFoodFamily
from cssw.nutriment import CohenSpreadSheetNutriment

spread_sheet = CohenSpreadSheet()

CALORIES = CohenSpreadSheetNutriment.CALORIES
RED_MEAT = CohenSpreadSheetFoodFamily.REDMET

calories_into_red_meat = spread_sheet.get_nutriment_by_food_family(CALORIES, RED_MEAT)
print(calories_into_red_meat)
```

# Installation 

```bash
python setup.py bdist_egg
easy_install dist/Cohen_Spread_Sheet_Wrapper-0.1-py3.7.egg

python -c "import cssw"
```