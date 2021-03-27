import { getRepository, Repository } from 'typeorm'
import IAudioRepository from './interfaces/IAudioRepository'

import Audio from '../../models/Audio'
import CreateAudioDTO from '../../dtos/CreateAudioDTO'

export default class AudioRepository implements IAudioRepository {
  private ormRepository: Repository<Audio>

  constructor() {
    this.ormRepository = getRepository(Audio)
  }

  public findAll(): Promise<Audio[]> {
    return this.ormRepository.find()
  }

  public findByUser(id: string): Promise<Audio[]> {
    return this.ormRepository.find({ where: { user_id: id } })
  }

  public async create({ title, author, audio, user_id }: CreateAudioDTO): Promise<Audio> {
    const createAudio = this.ormRepository.create({ title, author, audio, user_id })
    const _audio = await this.ormRepository.create(createAudio)
    return _audio
  }

  public update({ id, audio, title, author, user_id }: Audio): Promise<Audio> {
    return this.ormRepository.save({ id, title, author, audio, user_id })
  }

  public async delete(id: string): Promise<void> {
    await this.ormRepository.delete(id)
  }
}
