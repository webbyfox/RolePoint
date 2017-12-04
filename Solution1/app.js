var myApp = angular.module('myApp', []);


myApp.controller("MyController",function($scope, $http){
   $http.get("data.json").success(function(response){ 
   $scope.data = response;
   $scope.orderStaff = 'name';
      
    });
 });