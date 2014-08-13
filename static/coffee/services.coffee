'use strict'

angular.module('cocktail.services', [])
  .service('Ingredients', ['ApiService', (ApiService) -> 
    this.search = (searchString, callback) ->
      ApiService.searchForIngredients(searchString, (error, response) ->
        uniques = []
        seen = {}

        for ingredient in response.result
          if ingredient.name2 && !seen[ingredient.name2]
            seen[ingredient.name2] = true
            uniques.push(ingredient)
          else if !seen[ingredient.name] && !seen[ingredient.name2]
            seen[ingredient.name] = true
            uniques.push(ingredient)

        callback(null, uniques))

      return this
  ])
  .service('Recipes', ['ApiService', (ApiService) ->
    this.search = (ingredients, callback) ->
      searchWords = getSearchWords(ingredients)
      ApiService.searchForRecipes(searchWords, callback)

    getSearchWords = (ingredients) ->
      searchWords = []

      for ingredient in ingredients
        if !ingredient.categorySearch
          name = if ingredient.name2 then ingredient.name2 else ingredient.name
          searchWords.push name
        searchWords.push ingredient.type.split(", ")...

      return searchWords

    return this
  ])
  .service('ApiService', ['$http', ($http) ->
    baseUrl = '/'

    GET = (url, config, callback) ->
      if config == undefined || config == null
        config = {}
      if config.params == undefined || config.params == null
        config.params = {}

      $http.get(url, config).
        success( (data) -> 
          callback(null, data)).
        error( (err) ->
          console.error("Failed request to ", config, err)
          callback(err, null))

    POST = (url, content, callback, config) ->
      if config == undefined || config == null
        config = {}
      if config.params == undefined || config.params == null
        config.params = {}
      $http.post(url, content, config).
        success( (data) ->
          callback(null, data)).
        error( (err) ->
          console.log(url, config)
          console.error("Failed request to ", config, err)
          callback(err, null))

    this.searchForIngredients = (searchString, callback) ->
      url = baseUrl + 'ingredients/' + searchString
      return GET(url, null, callback)

    this.searchForRecipes = (words, callback) ->
      url = baseUrl + 'recipesbyingredients?key=' + words.join(",")

      return GET(url, null, (error, data) ->
        if error != undefined && error != null 
          return callback(error, null)
          
        recipes = data.result[0].recipes
        return callback(error, recipes))

    return this
  ])