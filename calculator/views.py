from django.http import HttpResponse
from django.shortcuts import render
import copy

DATA = {
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
        'помидор, ломтик':  1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:


def home_views(request):
    template_name = 'calculator/index.html'

    context = {
        'title': 'Список рецептов',
        'recipe_list': DATA
    }

    return render(request, template_name, context)


def recipe_views(request, recipe_request):
    template_name = 'calculator/recipe.html'

    servings = request.GET.get('servings')
    recipe = copy.deepcopy(DATA.get(recipe_request))

    if servings:
        for ingredient, amount in recipe.items():
            recipe[ingredient] = round(recipe[ingredient] * int(servings), 1)


    context = {
        'title': recipe_request,
        'recipe': recipe,
        'servings': servings
    }

    return render(request, template_name, context)
