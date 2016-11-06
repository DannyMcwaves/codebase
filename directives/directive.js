/*
this file, just includes a list of some of
the directives that I will end up using a lot.
*/

var app = window.app;
var $ = window.jQuery;

// This is the slideIn and the slideOut directive.
// when ng-slide is true, the element slides in
// and slides out when it is false.
app.directive("ngSlide", function () {
	"use strict";
	return {
		restrict: "A",
		multiElement: true,
		link: function (scope, element, attr) {
			var el = element;
			scope.$watch(attr.ngSlide, function (value) {
				if (value) {
					$(el).slideDown(500);
				} else {
					$(el).slideUp(500);
				}
			});
		}
	};
});

// This is the fadeIn and the fadeOut directive.
// when ng-fade is true, the element fades in
// and fades out when it is false.
app.directive("ngFade", function () {
	"use strict";
	return {
		restrict: "A",
		multiElement: true,
		link: function (scope, element, attr) {
			var el = element;
			scope.$watch(attr.ngFade, function (value) {
				if (value) {
					$(el).fadeIn(500);
				} else {
					$(el).fadeOut(500);
				}
			});
		}
	};
});

// the alert directive element get either alert as an element name or attr
// it also gets a head that signifies the head of the alert button and the content is the alert
// message that makes up for the message you are trying to the element.
app.directive("alert", function () {
	"use strict";
	return {
		templateUrl: "../directives/alert.html",
		replace: true,
		restrict: "EA",
		transclude: true,
		scope: {
			topic: "@head"
		},
		link: function (scope, element, attr) {
			if ($(element).hasClass("alert-success")) {
				$("div.alert strong").addClass("text-success");
			} else if ($(element).hasClass("alert-info")) {
				$("div.alert strong").addClass("text-info");
			} else if ($(element).hasClass("alert-danger")) {
				$("div.alert strong").addClass("text-danger");
			} else if ($(element).hasClass("alert-warning")) {
				$("div.alert strong").addClass("text-warning");
			}
		}
	};
});

// just as the name suggests, this is just a jumbotron
// and works just like a jumbotron would.
// Just pass the name and the inner content.
app.directive("jumbotron", function () {
	"use strict";
	return {
		templateUrl: "../directives/jumbotron.html",
		replace: true,
		restrict: "EA",
		transclude: true,
		scope: {
			head: "@head"
		}
	};
});

// for this you need to pass the list of the nav items as a property to the scope object.
// and you nest the element in the controler and add a 'nav' attribute to the element
app.directive("nav", function () {
	"use strict";
	return {
		templateUrl: "../directives/nav.html",
		replace: true,
		restrict: "A"
	};
});

app.directive("card", function () {
	"use strict";
	return {
		templateUrl: "../directives/card.html",
		replace: true,
		restrict: "EA",
		transclude: true,
		scope: {
			head: "@",
			src: "@",
			header: "@",
			footer: "@"
		},
		controller: function ($scope) {
			$scope.boolimage = Boolean($scope.src);
			$scope.boolheader = Boolean($scope.header);
			$scope.boolfooter = Boolean($scope.footer);
		},
		link: function (scope, element, attrs) {
//			element.on("mouseenter", function () {
//				element.removeClass("bg-danger").addClass("bg-success");
//			}).on('mouseleave', function () {
//				element.removeClass("bg-success").addClass("bg-danger");
//			});
		}
	};
});
