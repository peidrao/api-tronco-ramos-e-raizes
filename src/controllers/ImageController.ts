import { Request, Response } from 'express'
import ImageRepository from '../repositories/ImageRepository/ImageRepository'
import UserRepository from '../repositories/UserRepository/UserRepository'
import CreateImageService from '../services/ImageService/CreateImageService'
import UpdateImageService from '../services/ImageService/UpdateImageService'
import Storage from '../utils/storage/Storage'

export default class ImageController {
  public async upload(request: Request, response: Response): Promise<Response> {
    const file = request.file.filename
    return response.json({ file })
  }

  public async create(request: Request, response: Response): Promise<Response> {
    const { title, author, name } = request.body

    const imageRepository = new ImageRepository()
    const userRepository = new UserRepository()
    const storage = new Storage()
    const createImageService = new CreateImageService(
      imageRepository,
      userRepository,
      storage
    )
    const user_id = request.user.id

    const _image = await createImageService.execute({
      title,
      author,
      name,
      user_id
    })

    return response.status(201).json(_image)
  }

  public async update(request: Request, response: Response): Promise<Response> {
    const { id } = request.params
    const { title, name, author } = request.body

    const imageRepository = new ImageRepository()
    const userRepository = new UserRepository()
    const updateAudioService = new UpdateImageService(
      imageRepository,
      userRepository
    )
    const user_id = request.user.id

    const _image = await updateAudioService.execute({
      id,
      title,
      name,
      author,
      user_id
    })

    return response.json(_image)
  }
}
