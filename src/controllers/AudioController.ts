import { Request, Response } from 'express'
import AudioRepository from '../repositories/AudioRepository/AudioRepository'
import UserRepository from '../repositories/UserRepository/UserRepository'
import CreateAudioService from '../services/AudioService/CreateAudioService'
import UpdateAudioService from '../services/AudioService/UpdateAudioService'
import Storage from '../utils/storage/Storage'

export default class AudioController {
  public async upload(request: Request, response: Response): Promise<Response> {
    const file = request.file.filename
    return response.json({ file })
  }

  public async create(request: Request, response: Response): Promise<Response> {
    const { title, author, audio } = request.body

    const audioRepository = new AudioRepository()
    const userRepository = new UserRepository()
    const storage = new Storage()
    const createAudioService = new CreateAudioService(
      audioRepository,
      userRepository,
      storage
    )
    const user_id = request.user.id

    const _audio = await createAudioService.execute({
      title,
      author,
      audio,
      user_id
    })

    return response.status(201).json(_audio)
  }

  public async update(request: Request, response: Response): Promise<Response> {
    const { id } = request.params
    const { title, audio, author } = request.body

    const audioRepository = new AudioRepository()
    const userRepository = new UserRepository()
    const updateAudioService = new UpdateAudioService(
      audioRepository,
      userRepository
    )
    const user_id = request.user.id

    const _audio = await updateAudioService.execute({
      id,
      title,
      audio,
      author,
      user_id
    })

    return response.json(_audio)
  }
}
