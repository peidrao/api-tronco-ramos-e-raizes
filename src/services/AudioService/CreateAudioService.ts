import AppError from '../../errors/AppError'
import Audio from '../../models/Audio'
import IAudioRepository from '../../repositories/AudioRepository/interfaces/IAudioRepository'
import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'
import IStorage from '../../utils/storage/IStorage'
import Storage from '../../utils/storage/Storage'
import UploadAudioService from './UploadAudioService'

interface IRequest {
  title: string
  author: string
  audio: string
  user_id: string
}

export default class CreateAudioService {
  private audioRepository: IAudioRepository;
  private userRepository: IUsersRepository;
  private storage: IStorage;

  constructor(
    audioRepository: IAudioRepository,
    userRepository: IUsersRepository,
    storage: IStorage
  ) {
    this.audioRepository = audioRepository
    this.userRepository = userRepository
    this.storage = storage
  }

  public async execute({
    author,
    title,
    audio,
    user_id
  }: IRequest): Promise<Audio> {
    const user = await this.userRepository.findById(user_id)
    console.log('teste12')
    if (!user) {
      throw new AppError('Usuário não encontrado', 400)
    }

    if (!(await this.storage.fileExists(audio, 'temp'))) {
      throw new AppError('Não existe esse áudio', 400)
    }

    try {
      const doc = await this.audioRepository.create({
        title,
        audio,
        author,
        user_id
      })

      const storage = new Storage()
      const uploadAudioService = new UploadAudioService(storage)
      uploadAudioService.execute(audio)
      return doc
    } catch (e) {
      console.log(e)
      throw new AppError(e.message, 500)
    }
  }
}
