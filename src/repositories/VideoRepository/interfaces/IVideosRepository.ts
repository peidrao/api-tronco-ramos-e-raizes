import CreateVideoDTO from '../../../dtos/CreateVideoDTO'
import Video from '../../../models/Video'

export default interface IVideosRepository {
  findById(id: string): Promise<Video | undefined>;
  findAll(): Promise<Video[]>;
  create(video: CreateVideoDTO): Promise<Video>;
  delete(id: string): Promise<void>;
  save(video: Video): Promise<Video>;
}
