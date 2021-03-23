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
    const userExists = await this.userRepository.findById(user_id)
    if (!userExists) {
      throw new AppError('Usuário não encontrado', 400)
    }
    /* Não aparece a mensagem de status  */
    const linkExists = await this.videoRepository.findByLink(link)
    if (linkExists) {
      throw new AppError('Já existe um vídeo com esse link', 301)
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
