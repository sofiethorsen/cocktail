'use strict';

/* Services */
angular.module('cocktail.services', [])
  .service('Ingredients', ['ApiService', function(ApiService) {

    this.search = function(searchString, callback) {
      ApiService.searchForIngredients(searchString, function(error, response) {
        var uniques = [];
        var seen = {};

        response.result.forEach(function(ingredient) {
          if (ingredient.name2 && !seen[ingredient.name2]) {
            seen[ingredient.name2] = true;
            uniques.push(ingredient);
          } else if (!seen[ingredient.name] && !seen[ingredient.name2]) {
            seen[ingredient.name] = true;
            uniques.push(ingredient);
          }
        });

        callback(null, uniques);
      });
    };

    return this;
  }])
  .service('ApiService', ['$http', function ($http) {
    var baseUrl = '/';

    function GET(url, config, callback) {
      if (config === undefined || config === null) {
        config = {};
      }
      if (config.params === undefined || config.params === null) {
        config.params = {};
      }
      $http.get(url, config).
      success(function(data) {
        callback(null, data);
        }).
        error(function(err) {
          console.error("Failed request to ", config, err);
          callback(err, null);
        });
    }

    function POST(url, content, callback, config) {
      if (config === undefined || config === null) {
        config = {};
      }
      if (config.params === undefined || config.params === null) {
        config.params = {};
      }
      $http.post(url, content, config).
      success(function(data) {
        callback(null, data);
        }).
        error(function(err) {
          console.log(url, config);
          console.error("Failed request to ", config, err);
          callback(err, null);
        });
    }

    this.searchForIngredients = function(searchString, callback) {
      var url = baseUrl + 'ingredients/' + searchString;
      return GET(url, null, callback);
    };

    return this;
  }]);