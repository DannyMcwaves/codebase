
$("p").click(function (event) {
    "use strict";
    $.get('/mi', function (res) {
        window.alert(res);
    });
});

// document.cookie = "my very own session";
// window.alert(document.cookie);
