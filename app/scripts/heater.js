var heaterApp = angular.module('heaterApp', []);

heaterApp.controller('HeaterCtrl', function($scope, $http) {
	$scope.answer = "Yes";
	$scope.on = function() {
		$http.put("/heater");
	};
	$scope.off = function() {
		$http.post('/heater');
	}
});
