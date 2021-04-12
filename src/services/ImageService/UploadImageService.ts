import IStorage from '../../utils/storage/IStorage'

export default class UploadImageService {
  private storage: IStorage;
  constructor(storage: IStorage) {
    this.storage = storage
  }

  public async execute(file: string): Promise<void> {
    this.storage.saveFile(file, 'image')
  }
}
