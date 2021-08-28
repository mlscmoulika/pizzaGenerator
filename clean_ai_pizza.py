import json

def main():
    clean = []

    with open("ai_pizza_dirty.json", "r", encoding="utf-8") as f:
        dirty = json.load(f)

    for recipe in dirty:
        clean_recipe = []
        for ingredient in recipe["ingredients"]:
            assert len(ingredient) == 4
            name = ingredient[2]
            clean_recipe.append(name)
        clean.append(clean_recipe)

    with open("ai_pizza_clean.json", "w", encoding="utf-8") as f:
        json.dump(clean, f, indent=4)

    return 0

if __name__ == "__main__":
    exit(main())