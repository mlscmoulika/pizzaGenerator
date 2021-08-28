import os.path
import json
from typing import Optional

MAP = [
    ["bbq topping", "bbq sósa"],
    ["havarti kryddostur"],
    ["almond"],
    ["pineapple", "ananas"],
    ["apple"],
    ["artichoke"],
    ["asparagus"],
    ["avocado"],
    ["banana"],
    ["basil"],
    ["bean"],
    ["bean_black"],
    ["beef", "hakk"],
    ["bacon", "beikonkurl", "beikonsneiðar"],
    ["bell_pepper", "paprika", "græn paprika"],
    ["black_pepper", "svartur pipar", "pepper"],
    ["black_tea"],
    ["blue_cheese"],
    ["broccoli"],
    ["rice", "brown_rice"],
    ["buckwheat"],
    ["butter"],
    ["buttermilk"],
    ["cabbage"],
    ["caraway"],
    ["caraway_seed"],
    ["carrot"],
    ["cauliflower"],
    ["cayenne"],
    ["celery"],
    ["cheddar", "cheddarostur"],
    ["cherry"],
    ["chicken", "fajitas kjúklingur", "vegan kjúklingur"],
    ["chile_oil"],
    ["chili", "chile", "chile_pepper", "chiliflögur", "ferskur chili"],
    ["chive_mince"],
    ["clove"],
    ["coconut"],
    ["cilantro", "coriander"],
    ["corn"],
    ["cornmeal"],
    ["cornstarch"],
    ["crab", "crabmeat", "crabmeat_flake"],
    ["cracker"],
    ["cranberry"],
    ["cream"],
    ["cream_cheese", "rjómaostur"],
    ["cucumber"],
    ["cumin"],
    ["dill"],
    ["dried_tomato", "hálfþurrkaðir tómatar"],
    ["dried_parsley"],
    ["egg", "eggs"],
    ["eggplant"],
    ["fennel"],
    ["fenugreek"],
    ["feta_cheese"],
    ["fig"],
    ["garlic", "hvítlaukur"],
    ["garlic_oil", "hvítlauksolía"],
    ["ginger"],
    ["gluten_flour"],
    ["goat_cheese"],
    ["grape"],
    ["green"],
    ["green_bell_pepper"],
    ["green_olive"],
    ["gum"],
    ["ham", "skinka"],
    ["honey"],
    ["jalapeno"],
    ["ketchup"],
    ["lamb"],
    ["lemon", "lemon_juice"],
    ["lettuce"],
    ["lime"],
    ["lobster"],
    ["macaroni"],
    ["mango"],
    ["marjoram"],
    ["mashed_potato"],
    ["mayonnaise"],
    ["meat"],
    ["date", "döðlur"],
    ["mint"],
    ["mozzarella", "mozzarella_cheese"],
    ["mushroom", "white_mushroom", "sveppir"],
    ["nachos", "nachos flögur"],
    ["nut_pine"],
    ["nutmeg"],
    ["olive", "svartar ólífur"],
    ["olive_oil", "oil"],
    ["onion"],
    ["orange"],
    ["oregano"],
    ["oyster"],
    ["parsley"],
    ["pasta"],
    ["peach"],
    ["peanut"],
    ["peanut_butter"],
    ["pear"],
    ["pecan"],
    ["pepperoni", "peperoni", "sterkt pepperoní"],
    ["pesto"],
    ["pimento"],
    ["piparostur"],
    ["pistachio"],
    ["plum"],
    ["pork", "pork_sausage", "pulled pork"],
    ["potato"],
    ["powder"],
    ["provolone_cheese"],
    ["pumpkin"],
    ["red_lentil"],
    ["red_onion", "rauðlaukur"],
    ["red_pepper"],
    ["rosemary"],
    ["rye_bread"],
    ["salad"],
    ["salami"],
    ["salsa"],
    ["salt"],
    ["sauce_pesto"],
    ["sauerkraut"],
    ["sausage"],
    ["scallion"],
    ["seafood"],
    ["seed"],
    ["sesame_oil"],
    ["sesame_seed"],
    ["shallot"],
    ["shiitake"],
    ["shortening"],
    ["shrimp"],
    ["smoked_salmon"],
    ["soy_sauce"],
    ["spaghetti"],
    ["spinach", "spínat"],
    ["squash"],
    ["sriracha"],
    ["starch"],
    ["steak"],
    ["sugar"],
    ["sweet_potato"],
    ["taco"],
    ["tarragon"],
    ["thyme"],
    ["tofu"],
    ["tomato"],
    ["tortilla"],
    ["turkey"],
    ["turmeric"],
    ["vegan_cheese", "vegan ostur"],
    ["vegetable_oil"],
    ["vinegar"],
    ["walnut"],
    ["wine"],
    ["yeast"],
    ["yogurt"],
    ["zucchini"],
]


def map_ingredient(ingredient: str) -> Optional[str]:
    for m in MAP:
        if ingredient.lower() in m:
            return next(iter(list(m)))


def main():
    clean_pizzas = []
    for clean_path in os.listdir("clean"):
        if not clean_path.endswith(".json"):
            continue
        with open(os.path.join("clean", clean_path)) as f:
            clean_pizzas += json.load(f)

    normalized = []
    for pizza in clean_pizzas:
        normalized_pizza = []
        for ingredient in pizza:
            mapped = map_ingredient(ingredient)
            if mapped is None:
                continue
            normalized_pizza.append(mapped)
        normalized.append(normalized_pizza)

    with open("normalized.json", "w", encoding="utf-8") as f:
        json.dump(normalized, f, indent=4)

    nums = {ingredient: i for i, ingredient in enumerate([names[0] for names in MAP])}
    with open("mapping.json", "w", encoding="utf-8") as f:
        json.dump(nums, f, indent=4)

    vectors = []
    for normalized_pizza in normalized:
        vector = [0] * len(nums)
        for ingredient in normalized_pizza:
            vector[nums[ingredient]] = 1
        vectors.append(vector)
    with open("vectors.json", "w", encoding="utf-8") as f:
        json.dump(vectors, f)

    print(f"{len(vectors)} data points")

    return 0


if __name__ == "__main__":
    exit(main())
