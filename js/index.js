var angular = window.angular,
	$ = window.jQuery,
	app = angular.module("app", ["ngRoute"]);


app.config(function ($routeProvider) {
    "use strict";
    $routeProvider
		.when("/", {
			templateUrl: "/home"
		});
	
});
