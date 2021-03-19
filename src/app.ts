
import 'reflect-metadata'
import express, { Request, Response, NextFunction } from 'express'
// import "./database";
// import routes from "./routes";

const app = express()

app.use(express.json())

app.listen(3333, () => {
  console.log('Running App')
})
