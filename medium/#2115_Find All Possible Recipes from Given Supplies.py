class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        canMake = dict.fromkeys(supplies, True)
        recipe_to_idx = {recipe:idx for idx, recipe in enumerate(recipes)}
        checkedRecipes = []
        visited = set()
        def check_recipe(recipe):
            if canMake.get(recipe, False):
                return True
            if recipe not in recipe_to_idx or recipe in visited:
                return False

            visited.add(recipe)
            canMake[recipe] = all(check_recipe(ingredient) for ingredient in ingredients[recipe_to_idx[recipe]])
            return canMake[recipe]


        for recipe in recipes:
            if check_recipe(recipe):
                checkedRecipes.append(recipe)
        
        return checkedRecipes
    # ref: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/solutions/6502156/find-all-possible-recipes-from-given-supplies

