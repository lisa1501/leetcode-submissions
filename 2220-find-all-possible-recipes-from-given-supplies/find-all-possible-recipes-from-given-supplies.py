class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingre_to_recipe = defaultdict(list)
        recipe_to_ingre = defaultdict(int)

        for recipe, ingredient in zip(recipes, ingredients):
            recipe_to_ingre[recipe] = len(ingredient)
            for ingre in ingredient:
                ingre_to_recipe[ingre].append(recipe)


        q = deque(supplies)
        result = []

        while q:
            for _ in range(len(q)):
                ingre = q.popleft()

                for recipe in ingre_to_recipe[ingre]:
                    recipe_to_ingre[recipe] -= 1

                    if recipe_to_ingre[recipe] == 0:
                        q.append(recipe)
                        result.append(recipe)

        return result