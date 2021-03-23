import AppError from '../../errors/AppError'

import Video from '../../models/Video'
import IVideosRepository from '../../repositories/VideoRepository/interfaces/IVideosRepository'

interface IRequest {
  id: string;
  title: string;
  description: string;
  link: string;
}

export default class UpdateVideoService {
  private videoRepository: IVideosRepository;

  constructor(videoRepository: IVideosRepository) {
    this.videoRepository = videoRepository
  }

  public async execute({
    id,
    title,
    description,
    link
  }: IRequest): Promise<Video> {
    const video = await this.videoRepository.findById(id)

    if (!video) {
      throw new AppError('Vídeo não encontrado!', 400)
    }

    if (link !== video.link) {
      const verifyLink = this.videoRepository.findByLink(link)
      if (!verifyLink) {
        throw new AppError('Link já está sendo usado usado', 400)
      }
    }

    video.title = title
    video.description = description
    video.link = link

    await this.videoRepository.save(video)

    return video
  }
}
