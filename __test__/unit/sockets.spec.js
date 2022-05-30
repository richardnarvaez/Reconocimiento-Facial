const request = require('supertest')
const { app, io } = require('../../src/app')

// Simular servidor
// const express = require('express')
// const router = require('../../src/routes/index.routes')
// const app = new express()
// app.use('/', router)

let server
beforeAll((done) => {
   server = request(app)
   // httpServer = http.createServer().listen();
   // httpServerAddr = httpServer.listen().address();
   // ioServer = ioBack(httpServer);
   done()
})

afterAll((done) => {
   // server.close()
   // console.log('END SOCKETS TEST')
   done()
})

describe('SOCKETS MAIN', () => {
   test('Connection to SOCKETS', async () => {
      // await io.emit('echo', 'Hello World')
      io.on('connection', (mySocket) => {
         console.log('SO', mySocket)
         expect(mySocket).toBeNull()
      })
   })
})
