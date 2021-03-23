import { Router } from 'express'
import userRoutes from './user'
import sessionRoutes from './session'
import videoRoutes from './video'

const prefix = '/api/v1'
const routes = Router()

routes.use(`${prefix}/users`, userRoutes)
routes.use(`${prefix}/session`, sessionRoutes)
routes.use(`${prefix}/video`, videoRoutes)

export default routes
