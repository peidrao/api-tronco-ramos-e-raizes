import AppError from '../../errors/AppError'
import Document from '../../models/Document'
import IDocumentRepository from '../../repositories/DocumentRepository/interfaces/IDocumentRepository'
import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'
import Storage from '../../utils/storage/Storage'
import UploadDocumentService from './UploadDocumentService'

interface IRequest {
  id: string
  document: string
  title: string
  author: string
  user_id: string
}

export default class UpdateDocumentService {
  private documentRepository: IDocumentRepository
  private userRepository: IUsersRepository

  constructor(
    documentRepository: IDocumentRepository,
    userRepository: IUsersRepository
  ) {
    this.documentRepository = documentRepository
    this.userRepository = userRepository
  }

  public async execute({
    id, document, title, author, user_id
  }: IRequest): Promise<Document> {
    const user = await this.userRepository.findById(user_id)

    if (!user) {
      throw new AppError('Usuário não encontrado', 400)
    }

    const doc = await this.documentRepository.findById(id)

    if (!doc) {
      throw new AppError('Documento não existe!', 404)
    }

    try {
      const newDocument = {
        ...doc,
        document,
        title,
        author
      }
      const updatedDocument = await this.documentRepository.update(newDocument)
      if (doc.document !== document) {
        const storage = new Storage()
        const uploadDocumentService = new UploadDocumentService(storage)
        uploadDocumentService.execute(document)
      }
      return updatedDocument
    } catch (e) {
      throw new AppError(e.message, 500)
    }
  }
}
