class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredient_to_recipes = defaultdict(list)
        recipe_to_ingredients_list = defaultdict(int)

        for recipe, ingredient in zip(recipes, ingredients):
            recipe_to_ingredients_list[recipe] = len(ingredient)
            for ingre in ingredient:
                ingredient_to_recipes[ingre].append(recipe)

        q = deque(supplies)
        result = []

        while q:
            for _ in range(len(q)):
                ingre = q.popleft()

                for recipe in ingredient_to_recipes[ingre]:
                    recipe_to_ingredients_list[recipe] -= 1

                    if recipe_to_ingredients_list[recipe] == 0:
                        q.append(recipe)
                        result.append(recipe)

        return result

        





                

        


        