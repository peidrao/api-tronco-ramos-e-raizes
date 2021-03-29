import CreateAudioDTO from '../../../dtos/CreateAudioDTO'
import Audio from '../../../models/Audio'

export default interface IAudioRepository {
  findAll(): Promise<Audio[]>;
  findByUser(id: string): Promise<Audio[]>;
  findById(id: string): Promise<Audio | undefined>;
  create(data: CreateAudioDTO): Promise<Audio>;
  update(audio: Audio): Promise<Audio>;
  delete(id: string): Promise<void>;
}
