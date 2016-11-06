var express = require('express');
var path = require('path');
var favicon = require('static-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var task = require('./routes/get');
var compression = require("compression");
var serveIndex = require("serve-index");
var app = express();
var errorHandler = require("errorhandler");
var ph = require("./routes/tasks");


// view engine setup
app.set("appName", "myCodebase");
app.set("x-powered-by", false);
app.set("env", "development");
app.set("view engine", "pug");
app.set("views", path.join(__dirname, "views"));
app.set("view cache", app.get("env") === "production");
app.set("json spaces", 4);
app.set("jsonp callback name", "cb");

// also setting up some middlewares.
app.use(compression({threshold: 1}));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use("/fonts", express.static("./fonts"));
app.use("/images",  express.static("./images"));
app.use("/js", express.static("./js"));
app.use("/css", express.static("./css"));
app.use("/filters", express.static("./filters"));
app.use("/controllers", express.static("./controllers"));
app.use("/directives", express.static("./directives"));
app.use("/services", express.static("./services"));
app.use("/modules", express.static("./modules"));

app.get("/", task);
app.get("/home", task);
app.get("/header", task);
app.get("/footer", task);
app.get("/path", ph);


app.use(errorHandler);

module.exports = app;
