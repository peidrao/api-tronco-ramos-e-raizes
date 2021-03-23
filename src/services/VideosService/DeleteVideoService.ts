import AppError from '../../errors/AppError'
import IVideosRepository from '../../repositories/VideoRepository/interfaces/IVideosRepository'
import VideoRepository from '../../repositories/VideoRepository/VideoRepository'

export default class DeletVideoService {
  private videoRepository: IVideosRepository;

  constructor(videoRepository: VideoRepository) {
    this.videoRepository = videoRepository
  }

  public async execute(id: string): Promise<void> {
    const video = await this.videoRepository.findById(id)

    if (!video) {
      throw new AppError('Vídeo não existe!', 400)
    }

    await this.videoRepository.delete(id)
  }
}
