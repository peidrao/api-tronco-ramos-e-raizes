import IStorage from '../../utils/storage/IStorage'

export default class UploadAudioService {
  private storage: IStorage;
  constructor(storage: IStorage) {
    this.storage = storage
  }

  public async execute(file: string): Promise<void> {
    console.log('audio')
    this.storage.saveFile(file, 'audio')
  }
}
