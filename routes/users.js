var express = require('express');
var router = express.Router();
var app = express();

/* GET users listing. */
router
    .get('/', function(req, res) {
        res.send('respond with a resource');
    })
    .param("name", function(req, res, next, name) {
        req.username = name;
        return next();
    })
    .get("/:name", function(req, res) {
        res.send(req.username);
    })

module.exports = router;
