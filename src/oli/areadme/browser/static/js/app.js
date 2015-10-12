'use strict';

var areadmeApp = angular.module('AReadme', ['ngRoute',
                                            'areadmeControllers',
                                            'xeditable',
                                            'ngSanitize',
                                            'MessageCenterModule']);

areadmeApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/readme', {
        templateUrl: '++resource++oli.areadme/tpls/readme.html',
        controller: 'AReadmeController'
      }).
      when('/readme/detail/:headingId', {
        templateUrl: '++resource++oli.areadme/tpls/heading-detail.html',
        controller: 'HeadingDetailController'
      }).
      when('/readme/:headingId', {
        templateUrl: '++resource++oli.areadme/tpls/readme.html',
        controller: 'AReadmeController'
      }).
      otherwise({
        redirectTo: '/readme'
      });
  }]);

areadmeApp.factory('AReadmeData', function($http) {
  var context_url = $('#readme_context_url').val();
  var data_content = $('#data_content').val() || '{}';
  var tiny_pattern = $('#tinymce_pattern').val() || '{}';
  var authenticator = $('input[name="_authenticator"]').val();
  var authenticated = $('input[name="_authenticated"]').val();

  var factory = {
    context_url: context_url,
    data_content: JSON.parse(data_content),
    tiny_pattern: JSON.parse(tiny_pattern),
    authenticator: authenticator,
    authenticated: authenticated
  };

  factory.doSave = function() {
    var data = $.param({
      data: angular.toJson(factory.data_content)
    });

    // We need csrf token here
    var post_url = factory.context_url + '/edit_data?_authenticator=' + factory.authenticator;
    return $http({
        method: 'POST',
        url: post_url,
        data: data,
        // Use headers that please zope :)
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
    });
  };

  return factory;
});

areadmeApp.directive('atinymce', ['$timeout', 'AReadmeData',
function ($timeout, AReadmeData) {
    return {
        restrict: 'E',
        require: 'ngModel',
        template: '<textarea></textarea>', // A template you create as a HTML file (use templateURL) or something else...
        link: function ($scope, $element, attrs, ngModel) {

            // Find the textarea defined in your Template
            var textarea = $element.find('textarea');

            // When your model changes from the outside, use ngModel.$render to update the value in the textarea
            var tiny_pattern = AReadmeData.tiny_pattern;
            tinymce.init(textarea, tiny_pattern.tiny);
            var editor = tinymce.activeEditor;

            ngModel.$render = function () {
                editor.setContent(ngModel.$viewValue.content);
            };

            editor.on('input', function () {
                var newValue = this.getContent();

                if (!$scope.$$phase) {
                    $scope.$apply(function () {
                      ngModel.$viewValue.content = newValue;
                    });
                }
            });
        }
    };
}]);

areadmeApp.directive('goBack', function($window){
  return function($scope, $element){
    $element.on('click', function(){
      $window.history.back();
    });
  };
});

areadmeApp.run(function(editableOptions) {
  editableOptions.theme = 'default'; // bootstrap3 theme. Can be also 'bs2', 'default'
});
