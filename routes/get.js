var express = require('express');
var router = express.Router();
var path = require("../nodes/dir/path");

/* GET home page. */

router
    .get('/', function(req, res) {
        res.render('index', { title: 'international love' });
    })
    .param("pathname", function (req, res, next, pathname) {
        req.pathname = pathname;
        next();
    })
    .get("/home", function (req, res) {
        res.render("home");
    })
    .get("/header", function(req, res) {
        res.render("head");
    })
    .get("/footer", function (req, res) {
        res.render("footer");
    })
    .get("/path/:pathname", function (req, res) {
        console.log(req.pathname);
        res.send("hey_cool");
    })


module.exports = router;
