import { Router } from 'express'
import userRoutes from './user'
import sessionRoutes from './session'
import videoRoutes from './video'
import documentRoutes from './document'
import audioRoutes from './audio'

import imageRouters from './image'

const prefix = '/api/v1'
const routes = Router()
routes.use(`${prefix}/users`, userRoutes)
routes.use(`${prefix}/session`, sessionRoutes)
routes.use(`${prefix}/video`, videoRoutes)
routes.use(`${prefix}/document`, documentRoutes)
routes.use(`${prefix}/audio`, audioRoutes)
routes.use(imageRouters)

export default routes
