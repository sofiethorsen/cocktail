'use strict'

specialCases = {
      'Rom, Ljus rom' : 'ljus rom',
      'Rom, Mörk rom' : 'mörk rom',
      'Vin, Rött vin' : 'rött vin',
      'Vin, Vitt vin' : 'vitt vin',
      'Öl, Ljus öl' : 'ljus öl',
      'Öl, Mörk öl' : 'mörk öl'
}

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

    this.getRecipeInfo = (recipe, callback) ->
      ApiService.searchForRecipe(recipe, callback)

    getSearchWords = (ingredients) ->
      searchWords = []

      for ingredient in ingredients
        if !ingredient.categorySearch
          name = if ingredient.name2 then ingredient.name2 else ingredient.name
          searchWords.push name

        if specialCases.hasOwnProperty(ingredient.type)
          searchWords.push specialCases[ingredient.type]
        else 
          searchWords.push ingredient.type.split(", ")...

      return searchWords

    return this
  ])
  .service('ApiService', ['$http', ($http) ->
    baseUrl = '/'

    GET = (url, callback) ->
      $http.get(url).
        success( (data) -> 
          callback(null, data)).
        error( (err) ->
          console.error("Failed request to ", err)
          callback(err, null))

    this.searchForIngredients = (searchString, callback) ->
      url = baseUrl + 'ingredients/' + searchString
      return GET(url, callback)

    this.searchForRecipe = (name, callback) ->
      url = baseUrl + 'recipe/' + name
      return GET(url, callback)

    this.searchForRecipes = (words, callback) ->
      url = baseUrl + 'recipesbyingredients?key=' + words.join(",")

      return GET(url, (error, data) ->
        if error != undefined && error != null 
          return callback(error, null)
          
        recipes = data.result[0].recipes
        return callback(error, recipes))

    return this
  ])