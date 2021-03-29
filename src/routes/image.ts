import { Router, static as staticFiles } from 'express'
import { join } from 'path'

const imageRouters = Router()

imageRouters.use(staticFiles(join(__dirname, '..', '..', 'tmp', 'images')))

export default imageRouters