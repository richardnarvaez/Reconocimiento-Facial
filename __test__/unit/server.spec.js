const request = require('supertest')
const { app } = require('../../src/app')

// Simular servidor
// const express = require('express')
// const router = require('../../src/routes/index.routes')
// const app = new express()
// app.use('/', router)

describe('SERVER IS WORKING', () => {
   test('Responds to /', async () => {
      const res = await request(app).get('/')
      expect(res.header['content-type']).toBe('text/html; charset=utf-8')
      expect(res.statusCode).toBe(200)
      expect(res.text).toEqual('<h1>Hello world</h1>')
   })
   test('Responds to /conectar', async () => {
      const res = await request(app).get('/conectar')
      expect(res.header['content-type']).toBe('text/html; charset=utf-8')
      expect(res.statusCode).toBe(200)
      expect(res.text).toEqual('<h1>Conectado</h1>')
   })
})
