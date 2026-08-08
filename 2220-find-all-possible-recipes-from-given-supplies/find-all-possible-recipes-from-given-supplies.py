class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Topological Sort graph modeling 
        # build two grpah, 
        # 1st: one recipe to len ingredient, 
        # 2nd: one ingredient to list of recipe
        # store supplies in a queue
        # empty list all the recipes that we can create
        # popleft queue, supplie => ingredient
        # loop thru all recipe of supplie in 2nd grpah[ingredient], 
        # decrease len ingredients in 1st grpah[recipe],
        # after decreasing, if 1st grpah[recipe] ==0, queue append recipe, list append recipe
        # return the created list
        # time:O(R + I + S) space:O(R + I + S) R: total recipes, I: total ingredients, S: total supplies
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for recipe, ing_list in zip(recipes, ingredients):

            indegree[recipe] = len(ing_list)

            for ing in ing_list:
                graph[ing].append(recipe)

        queue = deque(supplies)

        result = []

        while queue:

            item = queue.popleft()

            for recipe in graph[item]:

                indegree[recipe] -= 1

                if indegree[recipe] == 0:

                    result.append(recipe)

                    queue.append(recipe)

        return result
        