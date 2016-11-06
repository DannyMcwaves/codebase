
var app = window.app;

app.filter("caps", function () {
	"use strict";
	return function (input) {
		var firstLetter = input.substring(0, 1).toUpperCase(),
			remaining = input.substring(1).toLowerCase();
		return firstLetter + remaining;
	};
});
