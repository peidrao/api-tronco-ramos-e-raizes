import { getRepository, Repository } from 'typeorm'
import CreateVideoDTO from '../../dtos/CreateVideoDTO'
import Video from '../../models/Video'
import IVideosRepository from './interfaces/IVideosRepository'

export default class VideoRepository implements IVideosRepository {
  private ormRepository: Repository<Video>;

  constructor() {
    this.ormRepository = getRepository(Video)
  }

  public findByLink(link: string): Promise<Video | undefined> {
    return this.ormRepository.findOne(link)
  }

  public async findById(id: string): Promise<Video | undefined> {
    const videoId = await this.ormRepository.findOne(id, {
      relations: ['user']
    })
    return videoId
  }

  public async findAll(): Promise<Video[]> {
    return this.ormRepository.find({ relations: ['user'] })
  }

  public async create({ title, link, description, user_id }: CreateVideoDTO): Promise<Video> {
    const video = this.ormRepository.create({
      title,
      link,
      description,
      user_id
    })
    await this.ormRepository.save(video)
    return video
  }

  public async delete(id: string): Promise<void> {
    await this.ormRepository.delete(id)
  }

  save(video: Video): Promise<Video> {
    return this.ormRepository.save(video)
  }
}
