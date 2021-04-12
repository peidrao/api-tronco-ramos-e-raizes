import AppError from '../../errors/AppError'
import Image from '../../models/Image'
import InterfaceImageRepository from '../../repositories/ImageRepository/interfaces/ImageRepository'
import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'
import Storage from '../../utils/storage/Storage'
import UploadImageService from './UploadImageService'

interface IRequest {
  id: string
  title: string
  author: string
  name: string
  user_id: string
}

export default class UpdateAudioService {
  private imageRepository: InterfaceImageRepository
  private userRepository: IUsersRepository

  constructor(
    imageRepository: InterfaceImageRepository,
    userRepository: IUsersRepository
  ) {
    this.imageRepository = imageRepository
    this.userRepository = userRepository
  }

  public async execute({
    id,
    name,
    title,
    author,
    user_id
  }: IRequest): Promise<Image> {
    const user = await this.userRepository.findById(user_id)

    if (!user) {
      throw new AppError('Usuário não encontrado', 400)
    }

    const _image = await this.imageRepository.findById(id)

    if (!_image) {
      throw new AppError('Áudio não encontrado!', 400)
    }

    try {
      const newImage = {
        ..._image,
        name,
        title,
        author
      }
      const updateImage = await this.imageRepository.update(newImage)
      if (_image.name !== name) {
        const storage = new Storage()
        const uploadAudioService = new UploadImageService(storage)
        uploadAudioService.execute(name)
      }
      return updateImage
    } catch (e) {
      throw new AppError(e.message, 500)
    }
  }
}
