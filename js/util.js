var $ = window.jQuery;

$(function () {
	"use strict";
	$('[data-toggle="tooltip"]').tooltip();
});


$(function () {
	"use strict";
	$('[data-toggle="popover"]').popover();
});

(function () {
    "use strict";

    $.fn.Height = function (sign, param) {
        var current = this;
        function keepHeight() {
            if (sign === "/" || sign === "div" || sign === "d") {
                $(current).height($(window).height() / param);
            } else if (sign === "+" || sign === "add" || sign === "a") {
                $(current).height($(window).height() + param);
            } else {
                $(current).css({
					minHeight: $(window).height()
				});
            }
        }
        $(window).resize(keepHeight);
        keepHeight();
        return $(this);
    };

    $.fn.Width = function (sign, param) {
        var current = this;
        function keepWidth() {
            if (sign === "/" || sign === "div" || sign === "d") {
                $(current).width($(window).width() / param);
            } else if (sign === "+" || sign === "add" || sign === "a") {
                $(current).width($(window).width() + param);
            } else {
                $(current).width($(window).width());
            }
        }
        $(window).resize(keepWidth);
        keepWidth();
        return $(this);
    };
	
	$.fn.abs = function () {
		$(this).css({
			position: "absolute",
			width: "100%"
		});
		return $(this);
	};
	
	$.fn.wrapAbs = function (obj) {
		var padding = $(this).height();
		$(this).wrap("<div class='wrapped rel width ' style='padding-bottom:" + padding / 2 + "px; padding-top:" + padding +  "px'>").css(obj).abs();
		return $(this);
	};
	
	$.size = function (callback) {
		var size;
		$(window).load(function () {
			if ($(window).width() <= 543) {
				size = "xs";
			} else if ($(window).width() >= 543 && $(window).width() <= 767) {
				size = "sm";
			} else if ($(window).width() >= 767) {
				size = "lg";
			}
			if (callback) {
				callback(size);
			}
			return;
		
		}).resize(function () {
			if ($(window).width() <= 543) {
				size = "xs";
			} else if ($(window).width() >= 543 && $(window).width() <= 767) {
				size = "sm";
			} else if ($(window).width() >= 767) {
				size = "lg";
			}
			if (callback) {
				callback(size);
			}
			return;
		});
	};
	
	$.scrolled = function (callback) {
		$(window).scroll(function () {
			if (callback) {
				callback($(window).scrollTop());
			}
			return;
		});
	};

}());


