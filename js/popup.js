var $ = window.jQuery;

(function () {
    "use strict";
    
    $.fn.addPopUp = function (text) {
        var canvas = "<canvas>sorry but your browser does not support canvas</canvas>";
        $("<div class='popup'>" + text + "</div>").css({
            position: "absolute",
            backgroundColor: "white",
            color: "#330033",
            padding: 10,
            minHeight: 100,
            minWidth: 250,
            maxWidth: 500
        }).append(canvas).prependTo($(this));
        
        var backcolor = $("div.popup").css("backgroundColor"),
            bordercolor = $("div.popup").css("borderColor"),
            canvs = $(this).find("canvas")[0],
            context = canvs.getContext("2d"),
            height = $(this).find("canvas").height(),
            width = $(this).find("canvas").width();
        
        context.beginPath();
        context.moveTo(150, 0);
        context.lineTo(300, 0);
        context.lineTo(30, 70);
        context.closePath();
        context.lineWidth = 2;
        context.strokeStyle = bordercolor;
        context.stroke();
        context.fillStyle = backcolor;
        context.fill();
        
        $(this).find("canvas").css({
            width: 50,
            height: 50,
            position: "absolute",
            bottom: -50,
            left: 20
        });
    };
}());