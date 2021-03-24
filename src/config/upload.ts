import multer from 'multer'
import crypto from 'crypto'
import path from 'path'

const tmp = path.resolve(__dirname, '..', '..', 'tmp')

const folders = {
  temp: tmp,
  document: path.resolve(tmp, 'documents')
}

export default {
  folders,
  storage: multer.diskStorage({
    destination: tmp,
    filename(request, file, callback) {
      const hash = crypto.randomBytes(8).toString('hex')
      const filename = `${hash}-${file.originalname}`

      return callback(null, filename)
    }
  })
}
