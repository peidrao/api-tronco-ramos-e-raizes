import 'reflect-metadata'
import 'express-async-errors'
import './database'
import express, { Response, Request, NextFunction } from 'express'
import routes from './routes'
import AppError from './errors/AppError'

const app = express()

app.use(express.json())
app.use(routes)

app.use((err: Error, request: Request, response: Response, _: NextFunction) => {
  if (err instanceof AppError) {
    return response
      .status(err.statusCode)
      .json({ status: 'error', message: err.message })
  }
  return response
    .status(500)
    .json({ status: 'Error', message: 'Internal server error' })
})

app.listen(3333, () => {
  console.log('Running App')
})
