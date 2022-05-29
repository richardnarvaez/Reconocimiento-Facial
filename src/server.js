const srv = require('./app')

srv.server.listen(3000, () => {
   console.log('>> Listening on *:3000')
})
