import { Router } from 'express'
import VideoController from '../controllers/VideoController'

import authenticate from '../middlewares/auth'
// import isSuper from '../middlewares/isSuper'

const videosRoutes = Router()
const videoController = new VideoController()

videosRoutes.use(authenticate)

videosRoutes.post('/', videoController.create)
videosRoutes.get('/', videoController.index)
videosRoutes.put('/:id', videoController.update)
videosRoutes.delete('/:id', videoController.destroy)

export default videosRoutes
