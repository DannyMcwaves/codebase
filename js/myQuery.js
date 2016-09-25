var myQuery = function (element, callback) {
    "use strict";
    
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

// i think so far for a rookie like me, i have made some very big strides 
// over here for myself an i think this will scale too.