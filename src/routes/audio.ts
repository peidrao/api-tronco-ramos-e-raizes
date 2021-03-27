import { Router } from 'express'
import multer from 'multer'
import upload from '../config/upload'
import AudioController from '../controllers/AudioController'

import authenticate from '../middlewares/auth'

const audioRoutes = Router()
const audioController = new AudioController()
const uploadFile = multer(upload)

audioRoutes.use(authenticate)

audioRoutes.post('/upload', uploadFile.single('file'), audioController.upload)
audioRoutes.post('/', audioController.create)
audioRoutes.put('/:id', audioController.update)

export default audioRoutes
