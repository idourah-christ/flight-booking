const express = require('express')
const cors = require("cors");
const server = require("./express-app");

const app = express()
const port = 8004

server(app)

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})