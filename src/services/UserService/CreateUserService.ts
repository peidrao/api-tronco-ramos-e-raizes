import { hash } from 'bcryptjs'
import AppError from '../../errors/AppError'
import User from '../../models/User'
import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'
import UserRepository from '../../repositories/UserRepository/UserRepository'

interface IRequest {
  name: string
  email: string
  password: string
}
export default class CreateUserService {
  private userRepository: IUsersRepository

  constructor (userRepository: UserRepository) {
    this.userRepository = userRepository
  }

  public async execute({ name, email, password }: IRequest): Promise<User> {
    const userEmail = await this.userRepository.findByEmail(email)

    if (userEmail) {
      throw new AppError('Email já cadastrado no sistema!', 404)
    }

    if (password.length <= 5) {
      throw new AppError('Senha curta demais', 400)
    }

    const passwordHash = await hash(password, 8)
    const user = await this.userRepository.create({ name, email, password: passwordHash })

    return user
  }
}
