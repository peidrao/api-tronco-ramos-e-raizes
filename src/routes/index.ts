import { Request, Response, Router } from 'express'
import userRoutes from './user'
import sessionRoutes from './session'
import videoRoutes from './video'
import documentRoutes from './document'
import multer from 'multer'
import uploadConfig from '../config/upload'
// import authenticate from '../middlewares/auth'

const prefix = '/api/v1'
const routes = Router()
/* const upload = multer(uploadConfig) */

/* routes.post('/upload', upload.single('file'),
  (request: Request, response: Response) => {
    const file = request.file.filename
    return response.json({ file })
  }
)
 */
routes.use(`${prefix}/users`, userRoutes)
routes.use(`${prefix}/session`, sessionRoutes)
routes.use(`${prefix}/video`, videoRoutes)
routes.use(`${prefix}/document`, documentRoutes)

export default routes
