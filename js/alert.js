var $ = window.$;

(function () {
    "use strict";
    
    $.alert = function (text) {
        if ($("div#alert").size() === 0) {
            $("<div id='alert'>" + text + "<p class='alertButton'><button>CLOSE</button></p></div>").css({
                position: "absolute",
                padding: 10,
                backgroundColor: "white",
                paddingBottom: 5,
                border: "2px solid #000000",
                color: "#333333",
                fontFamily: "Lato-Light"
            }).appendTo($("html"));
        }
        function left() {
            $("#alert").css({
                maxHeight: $(window).height() / 1.3,
                minWidth: $(window).width() / 4,
                maxWidth: $(window).width() / 1.8,
                left: $(window).width() / 3.5,
                top: $(window).height() / 6
            });
        }
        $(window).resize(left);
        left();
        
        $("p.alertButton").css({
            textAlign: "right"
        });
        function width() {
            $("p.alertButton").css({
                width: $("#alert").width(),
                marginTop: 5,
                marginBottom: 5
            });
        }
        $(window).resize(width);
        width();
        
        $("body").css({
            opacity: 0.3
        }).hideOverFlow();
        
        $("p.alertButton button").css({
            cursor: "pointer",
            padding: "3px 10px",
            backgroundColor: "black",
            color: "white",
            fontFamily: "Quicksand Regular"
        }).click(function (event) {
            $("#alert").remove();
            setTimeout(function () {
                $("body").css({
                    opacity: 1,
                    overflow: "auto"
                });
            }, 100);
        });
    };
    
}());