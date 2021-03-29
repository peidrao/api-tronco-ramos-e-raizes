import AppError from '../../errors/AppError'
import Audio from '../../models/Audio'
import IAudioRepository from '../../repositories/AudioRepository/interfaces/IAudioRepository'
import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'
import Storage from '../../utils/storage/Storage'
import UploadAudioService from './UploadAudioService'

interface IRequest {
  id: string;
  audio: string;
  title: string;
  author: string;
  user_id: string;
}

export default class UpdateAudioService {
  private audioRepository: IAudioRepository
  private userRepository: IUsersRepository

  constructor(
    audioRepository: IAudioRepository,
    userRepository: IUsersRepository
  ) {
    this.audioRepository = audioRepository
    this.userRepository = userRepository
  }

  public async execute({
    id,
    audio,
    title,
    author,
    user_id
  }: IRequest): Promise<Audio> {
    const user = await this.userRepository.findById(user_id)

    if (!user) {
      throw new AppError('Usuário não encontrado', 400)
    }

    const _audio = await this.audioRepository.findById(id)

    if (!_audio) {
      throw new AppError('Áudio não encontrado!', 400)
    }

    try {
      const newAudio = {
        ..._audio,
        audio,
        title,
        author
      }
      const updateAudio = await this.audioRepository.update(newAudio)
      if (_audio.audio !== audio) {
        const storage = new Storage()
        const uploadAudioService = new UploadAudioService(storage)
        uploadAudioService.execute(audio)
      }
      return updateAudio
    } catch (e) {
      throw new AppError(e.message, 500)
    }
  }
}
