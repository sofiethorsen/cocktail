'use strict';

/* Controllers */
angular.module('cocktail.controllers', [])
  .controller('SerachCtrl', ['$scope', 'Ingredients', function($scope, Ingredients) {
      $scope.ingredients = [];

      var searchIngredients = function(searchString) {
        Ingredients.search(searchString, function(err, ingredients) {
          $scope.articles = ingredients;
        });
      };

      $scope.removeIngredient = function(ingredient) {
        var index = $scope.ingredients.indexOf(ingredient);
        if (index > -1) {
          $scope.ingredients.splice(index, 1);
        }
      };

      /**
       * Adds an ingredient the users collection and initiate
       * a serach for new recipies.
       */
      $scope.addIngredient = function (ingredient) {
        $scope.ingredients.push(ingredient);
        $scope.ingredient = null;
        $scope.articles = [];
      };

      /**
       * When the value in the search field changes, this function is ran
       * and will initiate a search for ingredients if the input is valid.
       */
      $scope.onChange = function() {
        if($scope.ingredient === null || $scope.ingredient === undefined)
          return;
        if ($scope.ingredient.length > 1) {
          searchIngredients($scope.ingredient);
          console.log($scope.ingredient)
        }
        else {
          // If a new search isnt initiated, clear the result list.
          $scope.articles = [];
        }
      };

  }]);