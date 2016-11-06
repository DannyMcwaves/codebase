/*
    this is the simplest task ever.
    i am going to get some files over the network thingy and then be able to use.
    them in the browser. update them, delete then and then post new ones too.
*/

var express = require("express"),
    router = express.Router(),
    path = require("../nodes/dir/path");

router

    .get("/path", function (req, res) {
        p = path(req.query.pathname);
        rp = p.load().sread();

        if (!p.isFile()) {
            res.render("dir", {title: p.basename, path: p.pathname, main: path, content: rp})
        } else {
            rs = rp.toString()
            res.render("file", {title: p.basename, isFile: p.isFile(), path: p.pathname, main: path, content: rs});
        }
    })

module.exports = router;
