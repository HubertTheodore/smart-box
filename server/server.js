const express = require("express");
const bodyParser = require('body-parser')
const cors = require("cors")
const axios = require("axios")
const port = 8080
const app = express()
var x = ""
var y = ""
var direction = ""
var status = ""
var object = ""

app.use(cors())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

// handles get requests to backend
app.get("/api", (req, res)=>{
   // sends data to pico
   res.send({x: x, y: y, direction: direction})
   // changes data to empty string to avoid repeating commands
   x = ""
   y = ""
   direction = "" 
})

// handles post requests to backend
app.post("/api", (req, res)=>{
   // receives data from the front end and updates global variables that are used for the get request
   x = req.body.x
   y = req.body.y
   direction = req.body.direction
   status = req.body.status
   object = req.body.object
   // test response
   res.send({x: x, y: y, direction: direction, status: status, object: object})
   console.log(`x: ${x}, y: ${y}, direction: ${direction}, status: ${status}, object: ${object}`)
}) 
 
// listen on port 8080
app.listen(port, ()=>{
    console.log(`server is running on port ${port}`)
}) 
