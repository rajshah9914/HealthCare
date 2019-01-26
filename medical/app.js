var where = require('node-where');
 
where.is('4 yawkey way boston ma', function(err, result) {
  if (result) {
    console.log('Address: ' + result.get('address'));
    console.log('Street Number: ' + result.get('streetNumber'));
    console.log('Street: ' + result.get('street'));
    console.log('Full Street: ' + result.get('streetAddress'));
    console.log('City: ' + result.get('city'));
    console.log('State / Region: ' + result.get('region'));
    console.log('State / Region Code: ' + result.get('regionCode'));
    console.log('Zip: ' + result.get('postalCode'));
    console.log('Country: ' + result.get('country'));
    console.log('Country Code: ' + result.get('countryCode'));
    console.log('Lat: ' + result.get('lat'));
    console.log('Lng: ' + result.get('lng'));
  }
});
