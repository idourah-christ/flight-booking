const axios = require("axios");

const baseURL = 'http://127.0.0.1:8000/';

const axiosInstance = axios.create({
    baseURL:baseURL,
    headers:{
        "accept":'application/json'
    }
})

module.exports = axiosInstance;