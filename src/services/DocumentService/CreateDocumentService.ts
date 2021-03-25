import { container } from 'tsyringe'
import AppError from '../../errors/AppError'
import Document from '../../models/Document'
import IDocumentRepository from '../../repositories/DocumentRepository/interfaces/IDocumentRepository'
import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'
import IStorage from '../../utils/storage/IStorage'
import Storage from '../../utils/storage/Storage'
import UploadDocumentService from './UploadDocumentService'

interface IRequest {
  title: string
  author: string
  document: string
  user_id: string
}

export default class CreateDocumentService {
  private documentRepository: IDocumentRepository
  private userRepository: IUsersRepository
  private storage: IStorage

  constructor(
    documentRepository: IDocumentRepository,
    userRepository: IUsersRepository,
    storage: IStorage
  ) {
    this.documentRepository = documentRepository
    this.userRepository = userRepository
    this.storage = storage
  }

  public async execute({ author, title, document, user_id }: IRequest): Promise<Document> {
    const user = await this.userRepository.findById(user_id)
    console.log('teste12')
    if (!user) {
      throw new AppError('Usuário não encontrado', 400)
    }

    if (!(await this.storage.fileExists(document, 'temp'))) {
      throw new AppError('Não existe documento', 400)
    }

    try {
      const doc = await this.documentRepository.create({
        title,
        document,
        author,
        user_id
      })

      const storage = new Storage()
      const uploadDocumentService = new UploadDocumentService(storage)
      uploadDocumentService.execute(document)
      return doc
    } catch (e) {
      console.log(e)
      throw new AppError(e.message, 500)
    }
  }
}
