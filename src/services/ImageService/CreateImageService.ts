import AppError from '../../errors/AppError'
import Image from '../../models/Image'
import ImageRepository from '../../repositories/ImageRepository/interfaces/ImageRepository'
import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'
import IStorage from '../../utils/storage/IStorage'
import Storage from '../../utils/storage/Storage'
import UploadImageService from './UploadImageService'

interface IRequest {
  title: string
  author: string
  name: string
  user_id: string
}

export default class CreateAudioService {
  private imageRepository: ImageRepository;
  private userRepository: IUsersRepository;
  private storage: IStorage;

  constructor(
    imageRepository: ImageRepository,
    userRepository: IUsersRepository,
    storage: IStorage
  ) {
    this.imageRepository = imageRepository
    this.userRepository = userRepository
    this.storage = storage
  }

  public async execute({
    author,
    title,
    name,
    user_id
  }: IRequest): Promise<Image> {
    const user = await this.userRepository.findById(user_id)
    if (!user) {
      throw new AppError('Usuário não encontrado', 400)
    }

    const isFileExists = await this.storage.fileExists(name, 'temp')

    if (!isFileExists) {
      throw new AppError('Não existe essa imagem', 400)
    }

    try {
      const doc = await this.imageRepository.create({
        title,
        name,
        author,
        user_id
      })

      const storage = new Storage()
      const uploadImageService = new UploadImageService(storage)
      uploadImageService.execute(name)
      return doc
    } catch (e) {
      console.log(e)
      throw new AppError(e.message, 500)
    }
  }
}
