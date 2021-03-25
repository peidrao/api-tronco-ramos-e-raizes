import { getRepository, Repository } from 'typeorm'
import CreateDocumentDTO from '../../dtos/CreateDocumentDTO'
import Document from '../../models/Document'
import IDocumentRepository from './interfaces/IDocumentRepository'

export default class DocumentRepository implements IDocumentRepository {
  private ormRepository: Repository<Document>;

  constructor() {
    this.ormRepository = getRepository(Document)
  }

  public async findAll(): Promise<Document[]> {
    const documents = await this.ormRepository.find()
    return documents
  }

  public findByUser(id: string): Promise<Document[]> {
    return this.ormRepository.find({ where: { user_id: id } })
  }

  public async create({
    document,
    author,
    title,
    user_id
  }: CreateDocumentDTO): Promise<Document> {
    const createdDocument = this.ormRepository.create({
      document,
      title,
      author,
      user_id
    })
    const doc = await this.ormRepository.save(createdDocument)
    return doc
  }

  public update({
    id,
    title,
    author,
    document,
    user_id
  }: Document): Promise<Document> {
    return this.ormRepository.save({ id, title, author, document, user_id })
  }

  public async delete(id: string): Promise<void> {
    await this.ormRepository.delete(id)
  }
}
