'use strict';

angular.module('cocktail.controllers', [])
  .controller('SearchCtrl', ['$scope', 'Ingredients', 'Recipes', ($scope, Ingredients, Recipes) ->
      $scope.ingredients = []
      $scope.currentRecipe = {}
      $scope.currentRecipe['active'] = false

      searchIngredients = (searchString) ->
        Ingredients.search(searchString, (err, ingredients) ->
          $scope.articles = ingredients)

      $scope.removeIngredient = (ingredient) ->
        index = $scope.ingredients.indexOf(ingredient)
        if index > -1
          $scope.ingredients.splice(index, 1)
        if $scope.ingredients.length > 0
          searchRecipes($scope.ingredients)
        else
          $scope.recipes = null

      $scope.addIngredient = (ingredient) ->
        $scope.ingredients.push(ingredient)
        $scope.ingredient = null
        $scope.articles = []
        searchRecipes($scope.ingredients)

      $scope.onChange = () -> 
        if $scope.ingredient == null || $scope.ingredient == undefined
          return
        if $scope.ingredient.length > 1
          searchIngredients($scope.ingredient)
        else
          $scope.articles = []

      searchRecipes = (ingredients) ->
        Recipes.search(ingredients, (error, recipes) ->
          $scope.recipes = recipes)
  ])