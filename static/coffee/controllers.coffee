'use strict';

angular.module('cocktail.controllers', [])
  .controller('SearchCtrl', ['$scope', 'Ingredients', ($scope, Ingredients) ->
      $scope.ingredients = []

      searchIngredients = (searchString) ->
        Ingredients.search(searchString, (err, ingredients) ->
          $scope.articles = ingredients)

      $scope.removeIngredient = (ingredient) ->
        index = $scope.ingredients.indexOf(ingredient)
        if index > -1
          $scope.ingredients.splice(index, 1)

      $scope.addIngredient = (ingredient) ->
        $scope.ingredients.push(ingredient)
        $scope.ingredient = null
        $scope.articles = []

      $scope.onChange = () -> 
        if $scope.ingredient == null || $scope.ingredient == undefined
          return
        if $scope.ingredient.length > 1
          searchIngredients($scope.ingredient)
        else
          $scope.articles = []
  ])