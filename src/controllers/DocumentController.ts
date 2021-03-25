import { Request, Response } from 'express'
import DocumentRepository from '../repositories/DocumentRepository/DocumentRepository'
import UserRepository from '../repositories/UserRepository/UserRepository'
import CreateDocumentService from '../services/DocumentService/CreateDocumentService'
import Storage from '../utils/storage/Storage'

export default class DocumentController {
  public async upload(request: Request, response: Response): Promise<Response> {
    const file = request.file.filename
    console.log('teste')
    return response.json({ file })
  }

  public async create(request: Request, response: Response): Promise<Response> {
    const { title, document, author } = request.body
    console.log('Ok')

    const documentRepository = new DocumentRepository()
    const userRepository = new UserRepository()
    const storage = new Storage()
    const createDocumentService = new CreateDocumentService(documentRepository, userRepository, storage)
    const user_id = request.user.id

    const doc = await createDocumentService.execute({
      title,
      document,
      author,
      user_id
    })

    return response.status(201).json(doc)
  }
}
