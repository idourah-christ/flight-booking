const cors = require("cors");
const express = require("express");
const {flight} = require('./api');


module.exports = async (app) => {
    app.use(cors())
    app.use(express.json());

    //api
    flight(app);
}

