from django.http import HttpResponse
from django.shortcuts import render

def recipes(request, recipe_name, servings=1):
    all_recipes = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        }
    }
    recipe = all_recipes.get(recipe_name)
    if recipe and servings > 1:
        recipe = {
            ingredient: amount * servings for ingredient, amount in recipe.items()
        }
    context = {
        'recipe': recipe,
        'servings': servings
    }

    return render(request, 'calculator/index.html', context)

