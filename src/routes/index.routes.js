const { Router } = require('express')
const rt = Router()

rt.get('/', (req, res) => {
   res.send('<h1>Hello world</h1>')
})

module.exports = rt
