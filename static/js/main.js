/**
 * Created by florije on 2014/12/12.
 */
var app = angular.module('todoApp', []);

app.controller('IndexController', function ($scope) {
    $scope.onIndex = function(){
        $http({
            method: 'GET',
            url: '/'
        }).success(function(data){
            window.alert(data)
        })
    }
});