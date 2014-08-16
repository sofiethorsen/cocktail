'use strict';

angular.module('cocktail.controllers', [])
  .controller('SearchCtrl', ['$scope', 'Ingredients', 'Recipes', ($scope, Ingredients, Recipes) ->
      $scope.ingredients = []
      $scope.currentRecipe = {}
      $scope.currentRecipe['active'] = false

      $scope.addIngredient = (ingredient) ->
        $scope.ingredients.push(ingredient)
        $scope.ingredient = null
        $scope.articles = []
        searchRecipes($scope.ingredients)

      $scope.closeOverlay = () ->
        $scope.currentRecipe['active'] = false

      $scope.getRecipe = (recipe) ->
        getRecipeInfo(recipe[0])

      $scope.onChange = () -> 
        if $scope.ingredient == null || $scope.ingredient == undefined
          return
        if $scope.ingredient.length > 1
          searchIngredients($scope.ingredient)
        else
          $scope.articles = []

      $scope.removeIngredient = (ingredient) ->
        index = $scope.ingredients.indexOf(ingredient)
        if index > -1
          $scope.ingredients.splice(index, 1)
        if $scope.ingredients.length > 0
          searchRecipes($scope.ingredients)
        else
          $scope.recipes = null

      getRecipeInfo = (recipe) ->
        Recipes.getRecipeInfo(recipe, (error, info) ->
          $scope.currentRecipe['name'] = info['result']['name']
          $scope.currentRecipe['description'] = info['result']['description']
          $scope.currentRecipe['ingredients'] = info['result']['ingredients']
          $scope.currentRecipe['active'] = true
          )

      searchIngredients = (searchString) ->
        Ingredients.search(searchString, (error, ingredients) ->
          $scope.articles = ingredients)

      searchRecipes = (ingredients) ->
        Recipes.search(ingredients, (error, recipes) ->
          $scope.recipes = recipes)
  ])