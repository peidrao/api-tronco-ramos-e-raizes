import { Request, Response } from 'express'
import AudioRepository from '../repositories/AudioRepository/AudioRepository'
import UserRepository from '../repositories/UserRepository/UserRepository'
import CreateAudioService from '../services/AudioService/CreateAudioService'
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
    const createAudioService = new CreateAudioService(audioRepository, userRepository, storage)
    const user_id = request.user.id

    const _audio = await createAudioService.execute({ title, author, audio, user_id })

    return response.status(201).json(_audio)
  }
}
