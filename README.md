# Cohen Spread Sheet Wrapper 

:fr:

"Wrapper" du tableau Excel du Docteur Jean-Michel Cohen référencent les différentes quantités de nutriments que contient un aliment classés par famille d'aliments.

:uk:

A wrapper to use the spread sheet of Dr. Jean-Michel Cohen concerning nutrition nutriments quantity per food family.

# Example :uk: | Exemple :fr:

```python
from cssw import CohenSpreadSheet
from cssw import Food
from cssw import Nutriment

sheet = CohenSpreadSheet()
calories_into_red_meat = sheet.get_nutriment_by_food_family(Nutriment.CALORIES, Food.EGGANDMILK)
print(calories_into_red_meat)
```

# Installation 

```bash
# With Poetry package manager
poetry build
```