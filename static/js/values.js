angular.module('cocktail.values', [])
  // Doing this since systembolagets categories isn't that great,
  // if encountered by these categories, use the most specific
  // search term.
  .value("SpecialCases", {
      'Rom, Ljus rom' : 'ljus rom',
      'Rom, Mörk rom' : 'mörk rom',
      'Vin, Rött vin' : 'rött vin',
      'Vin, Vitt vin' : 'vitt vin',
      'Öl, Ljus öl' : 'ljus öl',
      'Öl, Mörk öl' : 'mörk öl'
    });
