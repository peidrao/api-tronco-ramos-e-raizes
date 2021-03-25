import IStorage from '../../utils/storage/IStorage'

export default class UploadDocumentService {
  private storage: IStorage
  constructor(storage: IStorage) {
    this.storage = storage
  }

  public async execute(file: string):Promise<void> {
    console.log('teste')
    this.storage.saveFile(file, 'document')
  }
}
