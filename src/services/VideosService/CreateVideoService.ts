import AppError from '../../errors/AppError'
import Video from '../../models/Video'
import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'
import IVideosRepository from '../../repositories/VideoRepository/interfaces/IVideosRepository'

interface IRequest {
  title: string;
  user_id: string;
  description: string;
  link: string;
}

export default class CreateVideoService {
  private videoRepository: IVideosRepository;

  private userRepository: IUsersRepository;

  constructor(
    videoRepository: IVideosRepository,
    userRepository: IUsersRepository
  ) {
    this.videoRepository = videoRepository
    this.userRepository = userRepository
  }

  public async execute({
    title,
    user_id,
    description,
    link
  }: IRequest): Promise<Video> {
    const verifyClient = await this.userRepository.findById(user_id)

    if (!verifyClient) {
      throw new AppError('Client não encontrado', 400)
    }
    const project = await this.videoRepository.create({
      title,
      user_id,
      description,
      link
    })
    return project
  }
}
