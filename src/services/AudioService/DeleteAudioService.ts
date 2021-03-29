import AppError from '../../errors/AppError'
import IAudioRepository from '../../repositories/AudioRepository/interfaces/IAudioRepository'
import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'

interface IRequest {
  id: string;
  user_id: string;
}

export default class DeleteAudioService {
  private audioRepository: IAudioRepository;
  private userRepository: IUsersRepository;

  constructor(
    audioRepository: IAudioRepository,
    userRepository: IUsersRepository
  ) {
    this.audioRepository = audioRepository
    this.userRepository = userRepository
  }

  public async execute({ id, user_id }: IRequest): Promise<void> {
    const user = await this.userRepository.findById(user_id)
    if (!user) {
      throw new AppError('Usuário não encontrado', 400)
    }

    const audio = await this.audioRepository.findById(id)
    if (!audio) {
      throw new AppError('Documento não encontrado', 400)
    }

    await this.audioRepository.delete(id)
  }
}
