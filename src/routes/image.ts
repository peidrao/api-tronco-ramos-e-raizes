import { Router, static as staticFiles } from 'express'
import multer from 'multer'
import { join } from 'path'

import upload from '../config/upload'
import ImageController from '../controllers/ImageController'

const imageRouters = Router()
const imageController = new ImageController()
const uploadFile = multer(upload)

imageRouters.use(staticFiles(join(__dirname, '..', '..', 'tmp', 'images')))
imageRouters.post('/upload', uploadFile.single('file'), imageController.upload)

export default imageRouters
