import AppError from '../../errors/AppError'
import IDocumentRepository from '../../repositories/DocumentRepository/interfaces/IDocumentRepository'
import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'

interface IRequest {
  id: string
  user_id: string
}

export default class DeleteDocumentService {
  private documentRepository: IDocumentRepository
  private userRepository: IUsersRepository

  constructor (documentRepository: IDocumentRepository, userRepository: IUsersRepository) {
    this.documentRepository = documentRepository
    this.userRepository = userRepository
  }

  public async execute({ id, user_id }: IRequest): Promise<void> {
    const user = await this.userRepository.findById(user_id)
    if (!user) {
      throw new AppError('Usuário não encontrado', 400)
    }

    const document = await this.documentRepository.findById(id)
    if (!document) {
      throw new AppError('Documento não encontrado', 400)
    }

    await this.documentRepository.delete(id)
  }
}
