import { Request, Response } from 'express'
import UserRepository from '../repositories/UserRepository/UserRepository'
import CreateUserService from '../services/UserService/CreateUserService'
import DeleteUserService from '../services/UserService/DeleteUserService'
import EnableSuperUserService from '../services/UserService/EnableSuperUserService'
import UpdateUserService from '../services/UserService/UpdateUserService'

export default class UserController {
  public async index(request: Request, response: Response): Promise<Response> {
    const userRepository = new UserRepository()
    const users = await userRepository.findAll()

    return response.json(users)
  }

  public async create(request: Request, response: Response): Promise<Response> {
    const { name, email, password } = request.body

    const userRepository = new UserRepository()
    const createUserService = new CreateUserService(userRepository)

    const user = await createUserService.execute({ name, email, password })

    // delete user.password

    return response.json(user)
  }

  public async update(request: Request, response: Response): Promise<Response> {
    const { id } = request.params
    const { name, email, password } = request.body

    const userRepository = new UserRepository()
    const updateUserService = new UpdateUserService(userRepository)

    const user = await updateUserService.execute({
      id,
      name,
      email,
      password
    })

    return response.status(201).json(user)
  }

  public async destroy(request: Request, response: Response): Promise<Response> {
    const { id } = request.params

    const userRepository = new UserRepository()
    const deleteUserService = new DeleteUserService(userRepository)

    await deleteUserService.execute(id)

    return response.status(204).send()
  }

  public async enableIsSuper(request: Request, response: Response): Promise<Response> {
    const { id } = request.params

    const userRepository = new UserRepository()
    const enableSuperUser = new EnableSuperUserService(userRepository)

    const user = await enableSuperUser.execute({ id })

    // delete user.password

    return response.json(user)
  }
}
