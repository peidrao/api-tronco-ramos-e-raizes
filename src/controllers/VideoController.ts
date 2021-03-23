import { Request, Response } from 'express'
import UserRepository from '../repositories/UserRepository/UserRepository'
import VideoRepository from '../repositories/VideoRepository/VideoRepository'
import CreateVideoService from '../services/VideosService/CreateVideoService'

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
}
