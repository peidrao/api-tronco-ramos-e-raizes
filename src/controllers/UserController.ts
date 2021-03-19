import { Request, Response } from 'express'
import UserRepository from '../repositories/UserRepository'
import CreateUserService from '../services/User/CreateUserService'

export default class UserController {
  public async create(request: Request, response: Response): Promise<Response> {
    const { name, email, password } = request.body

    const userRepository = new UserRepository()
    const createUserService = new CreateUserService(userRepository)

    const user = await createUserService.execute({ name, email, password })

    // delete user.password

    return response.json(user)
  }
}
