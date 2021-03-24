export type TFileType = | 'temp' | 'document'

export default interface IStorage {
  saveFile(file: string, fileType: TFileType): Promise<string>;
  deleteFile(file: string, fileType: TFileType): Promise<void>;
  fileExists(file: string, fileType: TFileType): Promise<boolean>;
}
