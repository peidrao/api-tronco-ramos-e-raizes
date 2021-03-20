import { Router } from 'express'
import userRoutes from './user'

const prefix = '/api/v1'
const routes = Router()

routes.use(`${prefix}/users`, userRoutes)

export default routes
