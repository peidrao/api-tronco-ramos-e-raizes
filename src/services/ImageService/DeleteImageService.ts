import AppError from '../../errors/AppError'
import InterfaceImageRepository from '../../repositories/ImageRepository/interfaces/ImageRepository'
import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'

interface IRequest {
  id: string;
  user_id: string;
}

export default class DeleteAudioService {
  private imageRepository: InterfaceImageRepository;
  private userRepository: IUsersRepository;

  constructor(
    imageRepository: InterfaceImageRepository,
    userRepository: IUsersRepository
  ) {
    this.imageRepository = imageRepository
    this.userRepository = userRepository
  }

  public async execute({ id, user_id }: IRequest): Promise<void> {
    const user = await this.userRepository.findById(user_id)
    if (!user) {
      throw new AppError('Usuário não encontrado', 400)
    }

    const image = await this.imageRepository.findById(id)
    if (!image) {
      throw new AppError('Documento não encontrado', 400)
    }

    await this.imageRepository.delete(id)
  }
}
