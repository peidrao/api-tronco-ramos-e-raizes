import fs from 'fs'
import path from 'path'
import IStorage, { TFileType } from './IStorage'
import uploadConfig from '../../config/upload'

export default class Storage implements IStorage {
  public async saveFile(file: string, fileType: TFileType): Promise<string> {
    fs.promises.rename(
      path.resolve(uploadConfig.folders.temp, file),
      path.resolve(uploadConfig.folders[fileType], file)
    )
    return file
  }

  public async deleteFile(file: string, fileType: TFileType): Promise<void> {
    const filePath = path.resolve(uploadConfig.folders[fileType], file)
    try {
      await fs.promises.stat(filePath)
    } catch {
    }
    await fs.promises.unlink(filePath)
  }

  public async fileExists(file: string, fileType: TFileType): Promise<boolean> {
    const filePath = path.resolve(uploadConfig.folders[fileType], file)
    try {
      await fs.promises.stat(filePath)
    } catch { return false }
    return true
  }
}
