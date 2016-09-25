/*
    this is the simplest task ever.
    i am going to get some files over the network thingy and then be able to use.
    them in the browser. update them, delete then and then post new ones too.
*/

var express = require("express"),
    router = express.Router(),
    path = require("./path/path.js");

router

    .param("user", function (req, res, next, user) {
        // res.send("welcome to your tasks");
        req.username = user;
        next();
    })
    .get("/", function (req, res){
        p = path()
        if (!p.isFile()) {
            res.render("dir", {title: p.basename, path: p.pathname, main: path, content: p.load().sread()})
        }
    })
    .get("/task", function (req, res) {
        console.log(req.Url);
        res.send("say, Hi there");
    })
    .get("/name", function (req, res){
        res.send("this is my name");
    })
    .get("/path", function (req, res) {
        // console.log(req.query);
        p = path(req.query.pathname);
        rp = p.load().sread();

        if (!p.isFile()) {
            res.render("dir", {title: p.basename, path: p.pathname, main: path, content: rp})
        }
        if (p.isFile()) {
            rs = rp.toString()
            res.render("file", {title: p.basename, isFile: p.isFile(), path: p.pathname, main: path, content: rs});
        }
    })

module.exports = router;
