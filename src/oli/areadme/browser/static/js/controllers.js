'use strict';

function randid() {
  return ((1 + Math.random()) * 1000000).toString(16).substring(1).replace('.', '');
}

var areadmeControllers = angular.module('areadmeControllers', []);

areadmeControllers.controller('AReadmeController', ['$scope', '$http', '$routeParams', 'messageCenterService', 'AReadmeData',
  function($scope, $http, $routeParams, messageCenterService, AReadmeData){
    $scope.context_url = AReadmeData.context_url;
    $scope.authenticator = AReadmeData.authenticator;
    $scope.authenticated = AReadmeData.authenticated;
    $scope.json_data = AReadmeData.data_content;
    $scope.save = AReadmeData.doSave;
    $scope.json_data.headings = $scope.json_data.headings || [];

    var current_id;
    if ($scope.json_data.headings.length) {
      current_id = $scope.json_data.headings[0].id;
    }
    if ($routeParams.headingId) {
      current_id = $routeParams.headingId;
    }
    $scope.cur_head = $.grep($scope.json_data.headings, function(e){ return e.id == current_id;})[0];

    $scope.addHeading = function(event, headingTitle){
      event.preventDefault();
      if ($scope.addheading) {

        if(this.headingTitle !== '' && $.grep($scope.json_data.headings, function(e){ return e.title == headingTitle;}).length <= 0){
          $scope.json_data.headings.push({
            'title': headingTitle,
            'content': '',
            'id':randid()
          });
        }
        this.headingTitle = '';
        $scope.addheading = false;
      } else {
        $scope.addheading = true;
      }
    };

    $scope.removeHeading = function(event, heading){
      event.preventDefault();
      $scope.json_data.headings = $.grep($scope.json_data.headings, function(e){ return e !== heading;});
      if ($scope.cur_head === heading) {
        $scope.cur_head = null;
      }
    };

    $scope.doSave = function() {
      $scope.save().then(function successCallback() {
        messageCenterService.add('success', 'Saved successfully', { timeout: 3000 });
        }, function errorCallback() {
          messageCenterService.add('danger', 'An error occured while saving', { timeout: 3000 });
        });
    };
}]);

areadmeControllers.controller('HeadingDetailController', ['$scope', '$routeParams', '$http', '$filter', 'AReadmeData',
  function($scope, $routeParams, $http, $filter, AReadmeData) {
    $scope.context_url = AReadmeData.context_url;
    $scope.authenticator = AReadmeData.authenticator;
    $scope.authenticated = AReadmeData.authenticated;
    $scope.json_data = AReadmeData.data_content;
    $scope.heading = $filter('filter')($scope.json_data.headings, {id: $routeParams.headingId})[0];
  }]);
