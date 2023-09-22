const axios = require("axios");

const baseURL = 'http://127.0.0.1:8000/api/';

const axiosInstance = axios.create({
    baseURL:baseURL,
    timeout: 500,
    headers:{
        // "Authorization":localStorage.getItem('access') ? `JWT ${localStorage.getItem('access')}` : null,
        "accept":'application/json'
    }
})

module.exports = axiosInstance;