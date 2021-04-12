import { getRepository, Repository } from 'typeorm'

import Image from '../../models/Image'
import CreateImageDTO from '../../dtos/CreateImageDTO'
import InterfaceImageRepository from './interfaces/ImageRepository'
import UserRepository from '../UserRepository/UserRepository'

export default class ImageRepository implements InterfaceImageRepository {
  private ormRepository: Repository<Image>;

  constructor() {
    this.ormRepository = getRepository(Image)
  }

  public findAll(): Promise<Image[]> {
    return this.ormRepository.find()
  }

  public findByUser(id: string): Promise<Image[]> {
    return this.ormRepository.find({ where: { user_id: id } })
  }

  public findById(id: string): Promise<Image | undefined> {
    return this.ormRepository.findOne(id)
  }

  public async create({
    title,
    author,
    name,
    user_id,
    album_id
  }: CreateImageDTO): Promise<Image> {
    const userRepo = new UserRepository()
    const user = await userRepo.findById(user_id)

    const createImage = this.ormRepository.create({
      title,
      author,
      name,
      user
    })
    const _image = await this.ormRepository.save(createImage)
    return _image
  }

  public update({ id, album, author, name, title, user }: Image): Promise<Image> {
    return this.ormRepository.save({
      id,
      album,
      title,
      author,
      name,
      user
    })
  }

  public async delete(id: string): Promise<void> {
    await this.ormRepository.delete(id)
  }
}
