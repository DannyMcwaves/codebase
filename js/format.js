(function () {
	"use strict";
	var myQuery,
		$,
		content,
		re,
		search,
		n_con,
		n_con2;

	// this is just a simple jquery-like tool. the format tool should depend on jquery but in case that is
	// non-existent, use myQuery.

	myQuery = function (element, callback) {
		// nl stands for node list
		var nl = window.document.querySelectorAll(element);

		if (element) {
			nl.forEach(function (e) {
				Object.defineProperties(e, {
					css : {
						value : function (css) {
							var keys = Object.keys(css);
							keys.forEach(function (prop) {
								e.style[prop] = css[prop];
							});
							return e;
						}
					},
					log : {
						value : function (message) {
							window.console.log(message);
							return e;
						}
					}
				});
				if (typeof callback === "function") {
					callback.apply(this, [e]);
				}
				return e;
			});
		} else {
			throw new Error("Argument Not a function");
		}

	};

	$ = window.jQuery || myQuery;
	// if you are using myQuery, then you need to be able to know how to get the text by writing your own function
	// and passing it as a callback to the myQuery function and then it gets executed.
	// I developed it to use it for an adhoc use purpose.

	content = $("div").text();
	re =  /(\b\n\b)|(\n)/g;
	n_con = content.replace(re, "<br>");

	n_con2 = n_con.replace(/\s{6,8}/g, "<span class='p-l-3'>").replace(/\s{4,6}/g, "<span class='p-l-2'>").replace(/\s{2,4}/g, "<span class='p-l-1'>");

	$("div#output").html(n_con2);

}());
