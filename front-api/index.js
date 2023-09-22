const express = require('express')
const cors = require('cors');
const proxy = require('express-http-proxy')

const app = express()
const port = 8003

app.use(cors());
app.use(express.json());

app.use("/flight", proxy('http://127.0.0.1:8000'));
app.use("/booking",proxy("http://127.0.0.1:8004"))

app.listen(port, () => {
  console.log(`booking.com gateway listening on port ${port}`)
})