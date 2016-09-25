var $ = window.$;
(function () {
    "use strict";
    $("#write").hide();
    $("a.yes").click(function () {
        $("section.message").slideUp("slow");
        $("#write").slideDown("slow");
    });
    $(window).ready(function () {
        var del = $("nav li").last();
        del.click(function (event) {
            var val = window.confirm("ARE YOU SURE YOU REALLY WANT TO DELETE THIS PAGE?");
            if (val === false) {
                event.preventDefault();
            }
        });
    });
    
    $("#write").submit(function (event) {
        var re = /PLEASE WRITE THE PAGE HERE[\s]*/;
        if (re.test($("#write textarea").val()) === true) {
            $("p.writeMessage").css({
                color: "red",
                fontFamily: "Quicksand-Regular",
                width: "90%",
                margin: "0px auto"
            }).html("Please clear the form and fill it with your content");
            event.preventDefault();
        }
//        alert(re.test($("#write textarea").val()));
    });

}());