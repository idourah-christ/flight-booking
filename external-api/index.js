const express = require('express')
const cors = require("cors");
const server = require("./express-app");

const app = express()
const port = 8006

server(app)

app.listen(port, () => {
  console.log(`External API running on port ${port}`)
})