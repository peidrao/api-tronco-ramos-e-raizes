import { hash } from 'bcryptjs'
import User from '../../models/User'
import IUsersRepository from '../../repositories/IUsersRepository'
import UserRepository from '../../repositories/UserRepository'

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

  public async execute ({ name, email, password }: IRequest): Promise<User> {
    const passwordHash = await hash(password, 8)

    const user = await this.userRepository.create({ name, email, password: passwordHash })

    return user
  }
}
