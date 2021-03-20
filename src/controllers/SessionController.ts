import { Request, Response } from 'express'
import UserRepository from '../repositories/UserRepository/UserRepository'
import LoginSessionService from '../services/SessionService/LoginSessionService'

export default class SessionController {
  public async login(request: Request, response: Response): Promise<Response> {
    const { email, password } = request.body

    const userRepository = new UserRepository()
    const loginSession = new LoginSessionService(userRepository)

    const session = await loginSession.execute({ email, password })

    // delete user.password

    return response.json(session)
  }
}
