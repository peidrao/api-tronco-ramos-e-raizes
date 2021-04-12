import { Router, static as staticFiles } from 'express'
import multer from 'multer'
import { join } from 'path'

import authenticate from '../middlewares/auth'
import upload from '../config/upload'
import ImageController from '../controllers/ImageController'

const imageRouters = Router()
const imageController = new ImageController()
const uploadFile = multer(upload)

imageRouters.use(authenticate)

imageRouters.use(staticFiles(join(__dirname, '..', '..', 'tmp', 'images')))
imageRouters.post('/upload', uploadFile.single('file'), imageController.upload)
imageRouters.post('/create', imageController.create)

export default imageRouters
