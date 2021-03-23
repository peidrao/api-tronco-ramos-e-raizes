import { Router } from 'express'
import VideoController from '../controllers/VideoController'

import authenticate from '../middlewares/auth'
// import isSuper from '../middlewares/isSuper'

const videosRoutes = Router()
const videoController = new VideoController()

videosRoutes.use(authenticate)

videosRoutes.post('/', videoController.create)

export default videosRoutes
