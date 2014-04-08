'use strict';

(function () {

  var app = angular.module('website', [
      'ngCookies',
      'ngResource',
      'ngSanitize',
      'ngRoute',
      'ui.bootstrap'
    ]);

  /*
   * Configuration
   */

  app.config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  });

  /*
   * Routing
   */

  app.config(function ($routeProvider, $locationProvider, urlconfig) {
    $locationProvider.html5Mode(true).hashPrefix('!');
    $routeProvider
      .when('/', {
        templateUrl: urlconfig.partials.prefix + 'index.html',
        controller: 'Homepage'
      })
      .otherwise({
        templateUrl: urlconfig.partials.prefix + '404.html',
        controller: 'NotFound'
      });
  });

  /*
   * Main Controller
   */

  app.controller('App', function ($scope) {

  });

  app.controller('Homepage', function ($scope) {
    // Homepage Ctrl
  });

  app.controller('NotFound', function ($scope) {
    // Page not found.
  });


})();
