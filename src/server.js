const { server } = require('./app')

const startServer = async (port) => {
   server.listen(port, () => {
      console.log('>> Listening on *:3000')
   })
}

startServer(3000)

module.exports = { startServer }
