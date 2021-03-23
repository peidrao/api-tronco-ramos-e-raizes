import { Request, Response } from 'express'
import UserRepository from '../repositories/UserRepository/UserRepository'
import VideoRepository from '../repositories/VideoRepository/VideoRepository'
import CreateVideoService from '../services/VideosService/CreateVideoService'
import ListAllVideoService from '../services/VideosService/ListAllVideoService'
import UpdateVideoService from '../services/VideosService/UpdateVideoService'
import DeleteVideoService from '../services/VideosService/DeleteVideoService'

export default class VideoController {
  public async create(request: Request, response: Response): Promise<Response> {
    const { title, user_id, description, link } = request.body

    const videoRepository = new VideoRepository()
    const userRepository = new UserRepository()
    const createVideo = new CreateVideoService(videoRepository, userRepository)

    const video = await createVideo.execute({
      title,
      user_id,
      description,
      link
    })

    return response.status(201).json(video)
  }

  public async update(request: Request, response: Response): Promise<Response> {
    const { id } = request.params
    const { title, description, link } = request.body

    const videoRepository = new VideoRepository()
    const updateVideoService = new UpdateVideoService(videoRepository)

    const video = await updateVideoService.execute({
      id,
      title,
      description,
      link
    })

    return response.status(201).json(video)
  }

  public async index(request: Request, response: Response): Promise<Response> {
    const videoRepository = new VideoRepository()
    const videoService = new ListAllVideoService(videoRepository)
    const videos = await videoService.execute()
    return response.json(videos)
  }

  public async destroy(request: Request, response: Response): Promise<Response> {
    const { id } = request.params
    const videoRepository = new VideoRepository()
    const videoService = new DeleteVideoService(videoRepository)
    await videoService.execute(id)
    return response.status(204).send()
  }
}
