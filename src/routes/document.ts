import { Router } from 'express'
import multer from 'multer'
import upload from '../config/upload'

import DocumentController from '../controllers/DocumentController'
import authenticate from '../middlewares/auth'

const documentRoutes = Router()
const documentController = new DocumentController()
const uploadFile = multer(upload)

documentRoutes.use(authenticate)
documentRoutes.post('/upload', uploadFile.single('file'), documentController.upload)
documentRoutes.post('/', documentController.create)
documentRoutes.put('/:id', documentController.update)

export default documentRoutes
