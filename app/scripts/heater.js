var heaterApp = angular.module('heaterApp', []);

heaterApp.controller('HeaterCtrl', function($scope, $http, $timeout) {
	$scope.answer = "Yes";
	$scope.on = function() {
		$http.put("/heater");
	};
	$scope.off = function() {
		$http.post('/heater');
	}

	$scope.temperature = 0;

	(function tick() {
		$http.get('/heater')
			.success(function (data) {$scope.temperature = data});
		$timeout(tick, 5000);
	})();
});
