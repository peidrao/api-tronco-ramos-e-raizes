import CreateDocumentDTO from '../../../dtos/CreateDocumentDTO'
import Document from '../../../models/Document'

export default interface IDocumentRepository {
  findAll(): Promise<Document[]>;
  findByUser(id: string): Promise<Document[]>
  create(document: CreateDocumentDTO): Promise<Document>;
  update(document: Document): Promise<Document>;
  delete(id: string): Promise<void>;
}
