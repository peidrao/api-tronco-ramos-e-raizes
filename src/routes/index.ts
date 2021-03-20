import { Router } from 'express'
import userRoutes from './user'
import sessionRoutes from './session'

const prefix = '/api/v1'
const routes = Router()

routes.use(`${prefix}/users`, userRoutes)
routes.use(`${prefix}/session`, sessionRoutes)

export default routes
