import CreateImageDTO from '../../../dtos/CreateImageDTO'
import Image from '../../../models/Image'

export default interface ImageRepository {
  findAll(): Promise<Image[]>;
  findByUser(id: string): Promise<Image[]>;
  findById(id: string): Promise<Image | undefined>;
  create(data: CreateImageDTO): Promise<Image>;
  update(image: Image): Promise<Image>;
  delete(id: string): Promise<void>;
}
