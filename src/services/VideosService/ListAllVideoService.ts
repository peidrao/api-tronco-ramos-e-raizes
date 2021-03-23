import Video from '../../models/Video'
import IVideosRepository from '../../repositories/VideoRepository/interfaces/IVideosRepository'

export default class ListAllVideoService {
  private videoRepository: IVideosRepository;

  constructor(videoRepository: IVideosRepository) {
    this.videoRepository = videoRepository
  }

  public async execute(): Promise<Video[]> {
    const videos = await this.videoRepository.findAll()
    return videos
  }
}
